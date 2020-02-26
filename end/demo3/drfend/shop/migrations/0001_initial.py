# Generated by Django 3.0.3 on 2020-02-26 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名')),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='商品名')),
                ('desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='描述')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category', verbose_name='分类')),
            ],
        ),
    ]
