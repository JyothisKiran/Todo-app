from django.urls import path
from .views import NoteListView, NoteCreateView


urlpatterns = [
    path('list/',NoteListView.as_view(),name='notes-list'),
    path('create/',NoteCreateView.as_view(),name='notes-create'),
]