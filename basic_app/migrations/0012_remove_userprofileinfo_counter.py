# Generated by Django 2.1 on 2018-08-22 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0011_auto_20180816_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='counter',
        ),
    ]