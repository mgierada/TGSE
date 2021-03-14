from django.contrib import admin
from .models import City, Transcript

# Register your models here.


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')


class TranscriptAdmin(admin.ModelAdmin):
    list_display = ('idd', 'date_published', 'audio_url', 'status')


admin.site.register(City, CityAdmin)
admin.site.register(Transcript, TranscriptAdmin)
