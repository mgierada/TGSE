from django.db import models


class City(models.Model):
    name = models.CharField(max_length=250)
    state = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class Transcript(models.Model):
    idd = models.CharField(max_length=240)
    date_published = models.CharField(max_length=241)
    text = models.TextField()
    audio_url = models.CharField(max_length=242)
    status = models.CharField(max_length=245)

    class Meta:
        verbose_name_plural = 'Transcripts'

    def __str__(self):
        return self.text


def populate_db():
    import os
    import re
    import json

    response_path = os.path.join(os.getcwd(), 'responses')

    for episode in os.listdir(response_path):
        print(episode)
        with open(os.path.join(response_path, episode), 'r') as f:
            data = json.load(f)

        audio_url = data['audio_url']
        date_tmp = re.search('cast(.*).mp3', audio_url)
        date_published = date_tmp.group(1)
        Transcript.objects.create(
            idd=data['id'],
            date_published=date_published,
            text=data['text'],
            audio_url=audio_url,
            status=data['status'],
        )


def clear_db():
    entries = Transcript.objects.all()
    entries.delete()


# populate_db()
# clear_db()
