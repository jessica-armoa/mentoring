# Generated by Django 4.2.5 on 2023-09-26 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_meetings_mentor_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]