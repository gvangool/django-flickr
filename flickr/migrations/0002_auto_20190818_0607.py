# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("flickr", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="sets",
            field=models.ManyToManyField(to="flickr.PhotoSet"),
        ),
        migrations.AlterField(
            model_name="jsoncache",
            name="added",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="photodownload",
            name="date_downloaded",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="photoset",
            name="photos",
            field=models.ManyToManyField(to="flickr.Photo", blank=True),
        ),
    ]
