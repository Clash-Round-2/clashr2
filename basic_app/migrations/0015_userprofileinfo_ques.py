# Generated by Django 2.1 on 2018-08-22 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0014_auto_20180822_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='ques',
            field=models.ManyToManyField(to='basic_app.Questions'),
        ),
    ]