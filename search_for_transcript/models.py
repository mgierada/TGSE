from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.utils import IntegrityError


class City(models.Model):
    name = models.CharField(max_length=250)
    state = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class Transcript(models.Model):
    episode_number = IntegerField(primary_key=True)
    date_published = CharField(max_length=10)
    link_to_mp3 = models.CharField(max_length=242)
    link_to_podcast = models.CharField(max_length=242)
    idd = models.CharField(max_length=240)
    status = models.CharField(max_length=245)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Transcripts'

    def __str__(self):
        return self.date_published


def populate_db():
    import os
    import re
    import json

    response_path = os.path.join(os.getcwd(), 'responses')

    for episode in os.listdir(response_path):
        print(episode)
        with open(os.path.join(response_path, episode), 'r') as f:
            data = json.load(f)

        link_to_mp3 = data['audio_url']
        date_tmp = re.search('cast(.*).mp3', link_to_mp3)
        date_published = date_tmp.group(1)
        Transcript.objects.create(
            idd=data['id'],
            date_published=date_published,
            text=data['text'],
            link_to_mp3=link_to_mp3,
            status=data['status'],
        )


def add_links_and_episodes_number():
    import os
    import json

    source_dir = os.path.join(os.getcwd(), 'source')
    all_podcast_data = 'all_podcasts_data.json'
    source_path = os.path.join(source_dir, all_podcast_data)

    with open(source_path, 'r') as f:
        episodes = json.load(f)

    for episode_number, inner_dict in episodes.items():
        date_published = inner_dict['date_published']
        link_to_mp3 = inner_dict['link_to_mp3']
        link_to_podcast = inner_dict['link_to_podcast']
        try:
            Transcript.objects.create(
                episode_number=episode_number,
                date_published=date_published,
                link_to_mp3=link_to_mp3,
                link_to_podcast=link_to_podcast,
            )
        except IntegrityError:
            print('Skipping episode #{} - episode already exists'.format(
                episode_number))
            pass


def add_response_results():
    import os
    import json

    response_path = os.path.join(os.getcwd(), 'responses')

    for episode in os.listdir(response_path):
        print(episode)
        with open(os.path.join(response_path, episode), 'r') as f:
            data = json.load(f)

        link_to_mp3 = data['audio_url']
        status = data['status']
        idd = data['id']
        text = data['text']

        Transcript.objects.filter(
            link_to_mp3=link_to_mp3).update(status=status, idd=idd, text=text)


def clear_db():
    entries = Transcript.objects.all()
    entries.delete()


# add_response_results()
# add_links_and_episodes_number()
# populate_db()
