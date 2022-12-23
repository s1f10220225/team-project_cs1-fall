from django.db import models

# Create your models here.
class Word(models.model):
    word = models.ChairField(max_length=999)
    meaning = models.TextField()
    test_num = models.IntegerField(default=0)
    genre = 
    favorite = models.IntegerField(default=0)