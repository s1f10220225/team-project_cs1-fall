from django.db import models

# Create your models here.
class Word(models.model):
    word = models.ChairField()
    meaning = models.TextField()
    test_num = models.IntegerField(default=0)
    genre = models.ChairField()
    favorite = models.IntegerField()

#genreとfavoriteは変えたほうがいいかも