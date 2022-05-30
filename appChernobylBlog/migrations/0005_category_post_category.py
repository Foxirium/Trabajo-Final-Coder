# Generated by Django 4.0.4 on 2022-05-30 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appChernobylBlog', '0004_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='category', max_length=255),
        ),
    ]
