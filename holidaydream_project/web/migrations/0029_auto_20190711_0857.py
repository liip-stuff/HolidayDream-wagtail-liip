# Generated by Django 2.2.2 on 2019-07-11 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('web', '0028_auto_20190711_0856'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FooterCustomSettings',
            new_name='NewsletterCustomSettings',
        ),
    ]