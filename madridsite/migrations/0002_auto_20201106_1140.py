# Generated by Django 3.0.7 on 2020-11-06 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madridsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='like_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]