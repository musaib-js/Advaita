# Generated by Django 4.1.5 on 2023-02-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='serial',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]