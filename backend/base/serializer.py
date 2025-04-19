from rest_framework import serializers
from .models import Note  # Import the Note model

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'description']  # ✅ match actual fields
