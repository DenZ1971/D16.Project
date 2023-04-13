# Generated by Django 4.1.7 on 2023-04-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0003_rename_author_advert_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="advert",
            name="upload",
            field=models.FileField(blank=True, null=True, upload_to="uploads/"),
        ),
        migrations.AlterField(
            model_name="advert", name="text", field=models.TextField(),
        ),
    ]
