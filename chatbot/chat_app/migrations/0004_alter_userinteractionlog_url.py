# Generated by Django 5.0.2 on 2024-03-03 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0003_userinteractionlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinteractionlog',
            name='url',
            field=models.URLField(null=True),
        ),
    ]