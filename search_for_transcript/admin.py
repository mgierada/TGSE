from django.contrib import admin
from .models import Transcript

# Register your models here.


class TranscriptAdmin(admin.ModelAdmin):
    list_display = ('episode_number', 'date_published',
                    'link_to_mp3', 'link_to_podcast', 'idd', 'status')


admin.site.register(Transcript, TranscriptAdmin)
