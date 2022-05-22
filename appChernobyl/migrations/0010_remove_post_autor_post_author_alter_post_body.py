# Generated by Django 4.0.4 on 2022-05-19 18:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appChernobyl', '0009_alter_stalkers_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='autor',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Random Stalker', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
    ]
