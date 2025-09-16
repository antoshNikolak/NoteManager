from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note
# Create your views here.

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # you can only call this roote if you are authenticated

    def get_queryset(self):
        user = self.request.user # get the current user
        return Note.objects.filter(author=user)
    
    # the bare minimum is to specify the serializer class permission class and queryset
    # this method is overriden because we want to include custom settings
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user # get the current user
        return Note.objects.filter(author=user)



class CreateUserView(generics.CreateAPIView):
    queryset  = User.objects.all() # returns list of User objects
    serializer_class = UserSerializer
    permission_classes = [AllowAny] # allow anyone to use this view to create a new user