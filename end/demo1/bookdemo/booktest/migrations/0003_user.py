# Generated by Django 3.0.3 on 2020-02-15 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_book_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(blank=True, max_length=11, null=True)),
            ],
        ),
    ]
