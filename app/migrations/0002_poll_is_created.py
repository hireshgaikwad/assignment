# Generated by Django 4.0.6 on 2022-07-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='is_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
