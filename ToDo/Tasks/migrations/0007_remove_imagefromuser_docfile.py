# Generated by Django 3.2.5 on 2022-02-08 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0006_imagefromuser_docfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagefromuser',
            name='docfile',
        ),
    ]