from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.TextField()
    meaning = models.TextField()
    test_num = models.IntegerField()
    genre = models.TextField()
    favorite =models.IntegerField() # 0=No, 1=Yes
    list_name = models.TextField()

class Test(models.Model):
    word = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    answer = models.TextField()
    correct_answer = models.TextField()