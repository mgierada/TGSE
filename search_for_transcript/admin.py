from django.contrib import admin
from .models import Transcript

# Register your models here.


class TranscriptAdmin(admin.ModelAdmin):
    list_display = ('idd', 'date_published', 'audio_url', 'status')


admin.site.register(Transcript, TranscriptAdmin)
