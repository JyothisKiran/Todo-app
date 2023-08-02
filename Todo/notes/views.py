from django.shortcuts import render
from .serializers import NoteSerializer
from .models import Notes
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class NoteListView(ListAPIView):
    serializer_class = NoteSerializer
    
    def get_queryset(self):
        queryset = Notes.objects.all().filter(user= self.request.user)
        return queryset


class NoteCreateView(CreateAPIView):
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
