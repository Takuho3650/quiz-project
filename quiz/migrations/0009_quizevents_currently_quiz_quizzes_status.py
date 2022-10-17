# Generated by Django 4.1.1 on 2022-10-17 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_userdata_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizevents',
            name='currently_quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='quiz.quizzes'),
        ),
        migrations.AddField(
            model_name='quizzes',
            name='status',
            field=models.IntegerField(choices=[(0, '出題前'), (1, '出題中'), (2, '回答受付中'), (3, '採点済み')], default=0, verbose_name='状態'),
        ),
    ]