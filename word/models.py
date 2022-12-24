from django.db import models

# Create your models here.


class Word(models.Model):
    word = models.CharField(max_length=225)
    meaning = models.TextField()
    test_num = models.IntegerField()
    genre = models.CharField(max_length=225)
    favorite = models.IntegerField(default=0)  # 0=No, 1=Yes
    list_name = models.CharField(max_length=225)


class Test(models.Model):
    word = models.CharField(max_length=225)
    option1 = models.CharField(max_length=225)
    option2 = models.CharField(max_length=225)
    option3 = models.CharField(max_length=225)
    option4 = models.CharField(max_length=225)
    answer = models.CharField(max_length=225)
    correct_answer = models.CharField(max_length=225)
