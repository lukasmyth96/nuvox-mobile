# Generated by Django 3.1.4 on 2021-01-17 12:29

from django.db import migrations, models
import keyboard.models


class Migration(migrations.Migration):

    dependencies = [
        ('keyboard', '0003_auto_20210103_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacollectionswipe',
            name='dataset_split',
            field=models.CharField(choices=[('train', 'train'), ('test', 'test')], default=keyboard.models.random_split, max_length=16),
        ),
    ]
