# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chirp', '0004_chirp_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('favorited_at', models.DateTimeField(auto_now_add=True)),
                ('chirp', models.ForeignKey(to='chirp.Chirp')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chirp',
            name='favorite_users',
            field=models.ManyToManyField(through='chirp.Favorite', related_name='chirps', to=settings.AUTH_USER_MODEL),
        ),
    ]
