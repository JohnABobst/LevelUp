# Generated by Django 2.2.1 on 2019-10-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20191019_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='next_level',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='user',
            name='xp',
            field=models.IntegerField(default=0),
        ),
    ]
