from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #related name is the field name we are adding to the user model to allow us to access all of its notes
    #cascade means if we delete a user we also delete all its notes

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        # is it bad practice to use self?
        return self.title