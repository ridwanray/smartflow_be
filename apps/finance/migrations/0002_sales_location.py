# Generated by Django 3.2 on 2022-07-12 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='location',
            field=models.TextField(default=''),
        ),
    ]