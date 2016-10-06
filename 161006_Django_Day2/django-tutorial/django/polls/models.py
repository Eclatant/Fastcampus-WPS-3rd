from django.db import models


class Question(models.Model):
    question_text = models.CharField('질문 내용', max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('선택한 내용', max_length=200)
    votes = models.IntegerField(default=0)