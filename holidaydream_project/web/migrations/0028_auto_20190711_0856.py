# Generated by Django 2.2.2 on 2019-07-11 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('web', '0027_auto_20190703_1440'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyCustomSettings',
            new_name='FooterCustomSettings',
        ),
    ]
