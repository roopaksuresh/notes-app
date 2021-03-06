from django.db import models
from django.utils import timezone


class Note(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    note = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def saved(self):
        self.saved_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
