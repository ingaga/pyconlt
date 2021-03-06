# Generated by Django 2.1.5 on 2019-02-17 14:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='audience_experience',
            field=models.IntegerField(choices=[(0, 'Junior'), (1, 'Intermediate'), (2, 'Expert')], default=0, help_text='Audience level'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='grant_description',
            field=models.CharField(blank=True, help_text='Short description about travel expenses or expected grant amount', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='proposal',
            name='speaker_grant',
            field=models.BooleanField(default=False, help_text='Check if you need a speaker grant'),
        ),
        migrations.AddField(
            model_name='proposal',
            name='target_audience',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Target audience', null=True),
        ),
    ]
