# Generated by Django 4.0.4 on 2022-05-22 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appChernobyl', '0016_artifact_delete_artifacts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artifact',
            old_name='disavantage',
            new_name='disadvantage',
        ),
    ]
