# Generated by Django 3.0.3 on 2020-02-23 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease_database', '0004_auto_20200223_1242'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DiseaseDatabaseModel',
            new_name='DatabaseFiles',
        ),
    ]