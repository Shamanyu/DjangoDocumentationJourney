# Manage database relations

from django.db import models

# Create your models here.

class Question(models.Model):

    # 'max_length' is a required field
    question_text = models.CharField(max_length=200)
    # Optional first argument 'date published' serves as human readable name
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):

    # Django supports all kinds of relationships(1:1, 1:N, M:N)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # 'default' is an optional field
    votes = models.IntegerField(default=0)
