from django.urls import path
from .views import NoteListView, NoteCreateView, NoteOperationsView


urlpatterns = [
    path('list/',NoteListView.as_view(),name='notes-list'),
    path('create/',NoteCreateView.as_view(),name='notes-create'),
    path('oper/<int:pk>/',NoteOperationsView.as_view(),name='notes-oper'),
]