# Generated by Django 3.1 on 2021-10-10 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='lastt_name',
            new_name='last_name',
        ),
    ]
