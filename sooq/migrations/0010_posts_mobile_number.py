# Generated by Django 3.2.3 on 2021-07-30 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sooq', '0009_auto_20210630_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='mobile_number',
            field=models.IntegerField(default=0),
        ),
    ]
