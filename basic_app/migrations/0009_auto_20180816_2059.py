# Generated by Django 2.1 on 2018-08-16 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0008_auto_20180815_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]