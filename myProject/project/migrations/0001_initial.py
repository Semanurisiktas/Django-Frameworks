# Generated by Django 4.1.2 on 2022-11-04 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('category', models.CharField(max_length=100, verbose_name='Category')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Image')),
            ],
        ),
    ]
