from rest_framework import serializers
from search_for_transcript.models import Transcript


class TranscriptSerializers_oldschool(serializers.Serializer):
    episode_number = serializers.IntegerField()
    date_published = serializers.CharField(max_length=10)
    link_to_mp3 = serializers.CharField(max_length=242)
    link_to_podcast = serializers.CharField(max_length=242)
    idd = serializers.CharField(max_length=240)
    status = serializers.CharField(max_length=245)
    text = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Transcript.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.episode_number = validated_data.get(
            'episode_number', instance.episode_number)
        instance.date_published = validated_data.get(
            'date_published', instance.date_published)
        instance.link_to_mp3 = validated_data.get(
            'link_to_mp3', instance.link_to_mp3)
        instance.link_to_podcast = validated_data.get(
            'link_to_podcast', instance.link_to_podcast)
        instance.idd = validated_data.get('idd', instance.idd)
        instance.status = validated_data.get('status', instance.status)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class TranscriptSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transcript
        fields = ['episode_number', 'date_published', 'link_to_mp3',
                  'link_to_podcast', 'idd', 'status', 'text']
