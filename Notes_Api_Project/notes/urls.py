from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NoteListCreateAPIView.as_view(), name='note-list'),
    path('notes/<int:pk>/', views.NoteDetailAPIView.as_view(), name='note-detail'),
    path('audio-notes/', views.AudioNoteCreateAPIView.as_view(), name='audio-note-create'),
    path('video-notes/', views.VideoNoteCreateAPIView.as_view(), name='video-note-create'),
]
