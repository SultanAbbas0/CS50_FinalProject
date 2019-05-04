from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    meaning = models.CharField(max_length=100)
    refrence = models.CharField(max_length=100, blank=True)
    sentence = models.CharField(max_length=255)

    def __str__(self):
        return self.word
