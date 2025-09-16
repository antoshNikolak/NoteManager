from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # model User is already pre existing in django
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}} # no one can ready what the password is. You can only create it upon signup

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}} # we manually set the author to whoever made it. We cannot pass this in as a field 
