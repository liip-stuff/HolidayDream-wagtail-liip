# Generated by Django 2.2.2 on 2019-07-02 13:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('web', '0018_formfield_formpage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FormPage',
            new_name='NewsletterFormPage',
        ),
    ]
