# Generated by Django 3.0.3 on 2020-02-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='polls',
            name='polls_1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='polls',
            name='polls_2',
            field=models.FloatField(default=0),
        ),
    ]