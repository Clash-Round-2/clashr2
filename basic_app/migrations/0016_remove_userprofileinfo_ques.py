# Generated by Django 2.1 on 2018-08-22 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0015_userprofileinfo_ques'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='ques',
        ),
    ]