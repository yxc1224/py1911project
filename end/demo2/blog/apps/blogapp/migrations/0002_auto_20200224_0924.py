# Generated by Django 3.0.3 on 2020-02-24 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default=None, max_length=20, verbose_name='标签名'),
        ),
    ]
