# Generated by Django 3.2.16 on 2023-01-14 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KGEprocess', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OCR_Queue',
            new_name='Queue',
        ),
        migrations.AlterModelTable(
            name='queue',
            table='queue',
        ),
    ]
