# Generated by Django 4.1.5 on 2023-02-06 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_sponsorship_remove_event_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='thumbnail',
            field=models.FileField(upload_to='media'),
        ),
    ]
