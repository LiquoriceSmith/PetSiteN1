# Generated by Django 4.0.5 on 2022-06-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, verbose_name='Вопрос')),
                ('answer1', models.CharField(max_length=200, verbose_name='1 вариант ответа')),
                ('answer2', models.CharField(max_length=200, verbose_name='2 вариант ответа')),
                ('answer3', models.CharField(max_length=200, verbose_name='3 вариант ответа')),
                ('right_answer', models.CharField(max_length=200, verbose_name='3 вариант ответа')),
            ],
        ),
    ]
