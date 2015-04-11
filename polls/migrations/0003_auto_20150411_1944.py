# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import polls.validators


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_pollster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollster',
            name='birthday',
            field=models.DateTimeField(verbose_name=b'Birthday', validators=[polls.validators.not_dead, polls.validators.not_future]),
            preserve_default=True,
        ),
    ]
