from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from audiofield.fields import AudioField
# from django.utils.translation import gettext_lazy as _

class Note(models.Model):
    TEXT = 'text'
    AUDIO = 'audio'
    VIDEO = 'video'
    NOTE_TYPES = [
        (TEXT, 'Text'),
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    note_type = models.CharField(max_length=10, choices=NOTE_TYPES, default=TEXT)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class AudioNote(models.Model):
    note = models.OneToOneField(Note, on_delete=models.CASCADE, primary_key=True)
    audio_file = AudioField(upload_to='audio_notes/', blank=True, null=True)

    def __str__(self):
        return self.note.title
    
class VideoNote(models.Model):
    note = models.OneToOneField(Note, on_delete=models.CASCADE, primary_key=True)
    video_url = EmbedVideoField()  # Stores the video URL

    def __str__(self):
        return self.note.title
