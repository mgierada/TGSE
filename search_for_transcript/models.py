from django.db import models
import json
import os

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=244)
    state = models.CharField(max_length=244)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class Transcript(models.Model):
    idd = models.CharField(max_length=244)
    text = models.CharField(max_length=244)
    audio_url = models.CharField(max_length=244)
    status = models.CharField(max_length=244)

    def __str__(self):
        return self.idd


def populate_db():
    response_path = os.path.join(os.getcwd(), 'responses')

    for episode in os.listdir(response_path):
        with open(os.path.join(response_path, episode), 'r') as f:
            data = json.load(f)

        Transcript.objects.create(
            idd=data['id'],
            text=data['text'],
            audio_url=data['audio_url'],
            status=data['status'])


def clear_db():
    entries = Transcript.objects.all()
    entries.delete()


# populate_db()
# clear_db()
