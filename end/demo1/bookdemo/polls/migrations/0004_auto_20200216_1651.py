# Generated by Django 3.0.3 on 2020-02-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200216_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollsmsg',
            name='coutmsg',
            field=models.FloatField(default=0, max_length=10, verbose_name='数量'),
        ),
    ]
