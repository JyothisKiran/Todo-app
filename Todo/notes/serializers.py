from rest_framework import serializers
from .models import Notes


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Notes
        fields = ['user', 'title', 'description']
        read_only_fields = ['user']