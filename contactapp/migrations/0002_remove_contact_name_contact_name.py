# Generated by Django 4.2.1 on 2023-05-29 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.AddField(
            model_name='contact',
            name='Name',
            field=models.CharField(default=None, max_length=10, unique=True),
        ),
    ]