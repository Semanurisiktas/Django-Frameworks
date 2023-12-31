# Generated by Django 4.1.2 on 2022-12-19 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('surname', models.CharField(max_length=100, verbose_name='Surname')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('comment', models.TextField(verbose_name='Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('tableNumber', models.IntegerField(default=1, primary_key=True, serialize=False, verbose_name='Table Number')),
                ('is_published', models.BooleanField(default=True, verbose_name='Published')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='menu', verbose_name='Image'),
        ),
        migrations.CreateModel(
            name='Rezervation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('surname', models.CharField(max_length=100, verbose_name='Surname')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('phoneNumber', models.CharField(max_length=100, verbose_name='Phone Number')),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('people', models.IntegerField(verbose_name='People')),
                ('table_number', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='project.table', verbose_name='Table')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.menu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
