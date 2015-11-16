# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chirp', '0002_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chirp',
            options={'ordering': ['-posted_at']},
        ),
    ]
