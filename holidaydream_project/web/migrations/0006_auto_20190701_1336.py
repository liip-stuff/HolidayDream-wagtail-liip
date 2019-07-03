# Generated by Django 2.2.2 on 2019-07-01 11:36

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20190701_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammemberpage',
            name='body',
            field=wagtail.core.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock(blank=True)), ('name', wagtail.core.blocks.CharBlock(blank=True)), ('paragraph', wagtail.core.blocks.CharBlock(blank=True))]),
        ),
    ]