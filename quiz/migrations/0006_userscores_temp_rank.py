# Generated by Django 4.1.1 on 2022-09-18 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_questions_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscores',
            name='temp_rank',
            field=models.IntegerField(default=-1, verbose_name='あなたの順位'),
        ),
    ]
