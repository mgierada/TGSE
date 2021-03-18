from django.db import models
from django.db.models.fields import CharField


class City(models.Model):
    name = models.CharField(max_length=250)
    state = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class Transcript(models.Model):
    episode_number = CharField(max_length=4)
    date_published = CharField(max_length=10)
    link_to_mp3 = models.CharField(max_length=242)
    link_to_podcast = models.CharField(max_length=242)
    idd = models.CharField(max_length=240)
    status = models.CharField(max_length=245)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Transcripts'

    def __str__(self):
        return self.idd


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


def clear_db():
    entries = Transcript.objects.all()
    entries.delete()


# populate_db()
