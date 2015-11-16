# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chirp', '0003_auto_20151026_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='chirp',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='chirp_images'),
        ),
    ]
