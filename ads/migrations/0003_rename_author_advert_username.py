# Generated by Django 4.1.7 on 2023-04-04 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0002_alter_advert_author_alter_response_sender_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="advert", old_name="author", new_name="username",
        ),
    ]
