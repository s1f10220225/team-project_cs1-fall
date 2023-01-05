from django.db import models

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=225, unique=True)

    def __str__(self):
        return self.genre
    

class Listinfo(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="Genre")
    list_num = models.IntegerField()
    list_name = models.CharField(max_length=225, null=True)

class Word(models.Model):
    word = models.CharField(max_length=255)
    meaning = models.TextField()
    belonging_list = models.ForeignKey(Listinfo, on_delete=models.CASCADE, related_name="list_info", null=True)

class Test(models.Model):
    word = models.CharField(max_length=225)
    option1 = models.CharField(max_length=225)
    option2 = models.CharField(max_length=225)
    option3 = models.CharField(max_length=225, null=True)
    option4 = models.CharField(max_length=225, null=True)
    answer = models.CharField(max_length=225)
    correct_answer = models.CharField(max_length=225)
