# Generated by Django 5.0.6 on 2024-05-26 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingtender',
            name='description',
            field=models.TextField(default='hello from tender description'),
        ),
    ]
