# Generated by Django 3.1.6 on 2021-05-11 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sooq', '0004_auto_20210509_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='who_send',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_posts', to='auth.user'),
            preserve_default=False,
        ),
    ]
