# Generated by Django 3.0.3 on 2020-02-15 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0004_account_concact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('sumary', models.TextField(verbose_name='正文')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签名')),
                ('articles', models.ManyToManyField(to='booktest.Article')),
            ],
        ),
    ]
