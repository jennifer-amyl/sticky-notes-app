from django.db import models

class Note(models.Model):
    """Model representing a note."""
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title