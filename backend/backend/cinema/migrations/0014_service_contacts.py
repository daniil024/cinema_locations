# Generated by Django 3.1.5 on 2021-04-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0013_auto_20210415_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='contacts',
            field=models.TextField(blank=True),
        ),
    ]
