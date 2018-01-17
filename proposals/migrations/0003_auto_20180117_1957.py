# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import proposals.models.attachment


class Migration(migrations.Migration):

    dependencies = [
        ('presenters', '0006_auto_20180113_1727'),
        ('proposals', '0002_proposal_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='presenter',
            field=models.ForeignKey(blank=True, help_text='Foreign key to presenter who proposed this talk/workshop', null=True, on_delete=django.db.models.deletion.CASCADE, to='presenters.Presenter'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='proposal',
            field=models.ForeignKey(help_text='Attachment of proposal', on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='proposals.Proposal'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='upload',
            field=models.FileField(upload_to=proposals.models.attachment.unique_dir_path),
        ),
    ]
