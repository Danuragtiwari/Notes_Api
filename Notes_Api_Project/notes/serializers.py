from rest_framework import serializers
from .models import Note, AudioNote, VideoNote


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'note_type', 'created_at']
        read_only_fields = ['id', 'created_at']


class AudioNoteSerializer(serializers.ModelSerializer):
    note = NoteSerializer()

    class Meta:
        model = AudioNote
        fields = ['note', 'audio_file']


class VideoNoteSerializer(serializers.ModelSerializer):
    note = NoteSerializer()

    class Meta:
        model = VideoNote
        fields = ['note', 'video_file']
