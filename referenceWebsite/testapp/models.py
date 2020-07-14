from django.db import models

# Create your models here.
class Test(models.Model):
    question1 = models.ForeignKey(Question, on_delete=models.CASCASE)
    question2 = models.ForeignKey(Question, on_delete=models.CASCASE)


class Question(models.Model):
    text = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

