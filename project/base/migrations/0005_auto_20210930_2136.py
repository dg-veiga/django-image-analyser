# Generated by Django 3.1.7 on 2021-09-30 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210925_0219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analysis',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='analysis',
            old_name='_type',
            new_name='tipo',
        ),
    ]