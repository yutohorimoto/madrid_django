# Generated by Django 3.0.7 on 2020-11-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madridsite', '0002_auto_20201106_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.TextField()),
                ('number', models.IntegerField(default=0)),
            ],
        ),
    ]
