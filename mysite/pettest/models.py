from django.db import models
from django.urls import reverse


# Create your models here.

class PetTest(models.Model):
    question = models.TextField(blank=True, verbose_name='Вопрос')
    answer1 = models.CharField(max_length=200, verbose_name='1 вариант ответа')
    answer2 = models.CharField(max_length=200, verbose_name='2 вариант ответа')
    answer3 = models.CharField(max_length=200, verbose_name='3 вариант ответа')
    right_answer = models.CharField(max_length=200, verbose_name='Правильный вариант ответа')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    question_text = models.CharField(max_length=300)


class Answers(models.Model):
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    answers = models.CharField(max_length=150)
    right_answer = models.CharField(max_length=150)


class UserAnswer(models.Model):
    user = models.CharField(max_length=200)
    # потом изменить  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.user