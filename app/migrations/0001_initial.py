# Generated by Django 4.1.2 on 2022-10-14 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rn', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]