# Generated by Django 4.0.5 on 2022-06-23 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pettest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='pettest',
            options={'verbose_name': 'Тест', 'verbose_name_plural': 'Тесты'},
        ),
        migrations.AlterField(
            model_name='pettest',
            name='right_answer',
            field=models.CharField(max_length=200, verbose_name='Правильный вариант ответа'),
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.CharField(max_length=150)),
                ('right_answer', models.CharField(max_length=150)),
                ('question_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pettest.question')),
            ],
        ),
    ]