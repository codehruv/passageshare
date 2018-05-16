from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

class Book(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.book_name

"""
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    book = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)
"""

