# Generated by Django 2.1.3 on 2018-12-25 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20181225_0727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='articleAuthor',
        ),
    ]
