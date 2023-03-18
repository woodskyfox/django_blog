from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# My models.

class BlogPost(models.Model):
    """A blog that user can write."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
