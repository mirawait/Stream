# Generated by Django 3.2.5 on 2021-07-21 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_watch_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='stream_key',
            field=models.TextField(unique=True),
        ),
    ]
