from django.shortcuts import render
from .serializers import NoteSerializer
from .models import Notes
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.


class NoteListView(ListAPIView):
    serializer_class = NoteSerializer
    
    def get_queryset(self):
        queryset = Notes.objects.all().filter(user= self.request.user)
        return queryset


class NoteCreateView(CreateAPIView):
    serializer_class = NoteSerializer
    queryset = Notes.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data['title']
        if self.queryset.filter(title=title).exists():
            raise ValidationError("Note with same title already exist")
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NoteOperationsView(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer

    def get_object(self,pk):
        try:
            note = Notes.objects.get(pk=pk)
            return note
        except Notes.DoesNotExist as e:
            return False

    def get(self, request, pk,*args, **kwargs):
        obj = self.get_object(pk)
        print(obj)
        if obj:
            serializer = self.serializer_class(instance=obj)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        