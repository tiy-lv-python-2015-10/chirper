# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chirp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('chirp', models.ManyToManyField(to='chirp.Chirp')),
            ],
        ),
    ]
