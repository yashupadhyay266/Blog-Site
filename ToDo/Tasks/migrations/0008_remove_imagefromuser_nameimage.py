# Generated by Django 3.2.5 on 2022-02-08 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0007_remove_imagefromuser_docfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagefromuser',
            name='nameimage',
        ),
    ]