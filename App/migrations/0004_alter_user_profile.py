# Generated by Django 4.2.3 on 2023-07-23 04:24

import PlacementFreak.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, null=True, storage=PlacementFreak.storage.MediaStorage(), upload_to=''),
        ),
    ]