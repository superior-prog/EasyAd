# Generated by Django 3.1.7 on 2021-04-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
