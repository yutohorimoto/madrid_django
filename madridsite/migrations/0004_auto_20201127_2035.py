# Generated by Django 3.0.7 on 2020-11-27 11:35

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('madridsite', '0003_election'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
