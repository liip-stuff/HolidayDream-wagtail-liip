# Generated by Django 2.2.2 on 2019-07-03 12:40

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0026_auto_20190703_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticpage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.CharBlock(blank=True)), ('lead', wagtail.core.blocks.CharBlock(blank=True)), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(blank=True)), ('quote', wagtail.core.blocks.BlockQuoteBlock(blank=True))]),
        ),
    ]