# Generated by Django 4.0 on 2022-01-14 09:45

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('care_groups', '0008_alter_caregroupmembership_care_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='caregroup',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='care_group_photos'),
        ),
    ]
