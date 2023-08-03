from .serializers import NoteSerializer
from .models import Notes
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.


class NoteListView(ListAPIView):
    serializer_class = NoteSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get_queryset(self):
        queryset = Notes.objects.all().filter(user=self.request.user)
        return queryset
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset
        return Response({'objects': queryset}, template_name='notes/list.html')


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

    def get_object(self, pk):
        try:
            note = Notes.objects.get(pk=pk)
            return note
        except Notes.DoesNotExist:
            return False

    def get(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        print(obj)
        if not obj:
            return Response(data="object not found", status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(instance=obj)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(obj, data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        obj = self.get_object(pk)
        if not obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_200_OK)
