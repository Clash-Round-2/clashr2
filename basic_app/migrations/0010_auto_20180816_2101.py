# Generated by Django 2.1 on 2018-08-16 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0009_auto_20180816_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='questions',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='questions',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='basic_app.Questions'),
        ),
    ]