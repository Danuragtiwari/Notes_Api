from rest_framework import generics, permissions
from .models import Note, AudioNote, VideoNote
from .serializers import NoteSerializer, AudioNoteSerializer, VideoNoteSerializer
from .permissions import IsOwnerOrReadOnly


class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class AudioNoteCreateAPIView(generics.CreateAPIView):
    queryset = AudioNote.objects.all()
    serializer_class = AudioNoteSerializer
    permission_classes = [permissions.IsAuthenticated]


class VideoNoteCreateAPIView(generics.CreateAPIView):
    queryset = VideoNote.objects.all()
    serializer_class = VideoNoteSerializer
    permission_classes = [permissions.IsAuthenticated]
