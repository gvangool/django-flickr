# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import taggit.managers
from django.conf import settings
from django.db import migrations, models

import flickr.models


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Collection",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "flickr_id",
                    models.CharField(unique=True, max_length=50, db_index=True),
                ),
                ("show", models.BooleanField(default=True)),
                (
                    "last_sync",
                    models.DateTimeField(null=True, editable=False, blank=True),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(null=True, blank=True)),
                ("icon", models.URLField(max_length=255, null=True, blank=True)),
                ("date_created", models.DateTimeField(null=True, blank=True)),
                ("parent", models.ForeignKey(to="flickr.Collection", null=True)),
            ],
            options={"ordering": ("-date_created",), "get_latest_by": "date_created"},
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="FlickrUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("flickr_id", models.CharField(max_length=50, null=True, blank=True)),
                ("nsid", models.CharField(max_length=32, null=True, blank=True)),
                ("username", models.CharField(max_length=64, null=True, blank=True)),
                ("realname", models.CharField(max_length=64, null=True, blank=True)),
                ("photosurl", models.URLField(max_length=255, null=True, blank=True)),
                ("profileurl", models.URLField(max_length=255, null=True, blank=True)),
                ("mobileurl", models.URLField(max_length=255, null=True, blank=True)),
                ("iconserver", models.CharField(max_length=4, null=True, blank=True)),
                ("iconfarm", models.PositiveSmallIntegerField(null=True, blank=True)),
                ("path_alias", models.CharField(max_length=32, null=True, blank=True)),
                ("ispro", models.NullBooleanField()),
                ("tzoffset", models.CharField(max_length=6, null=True, blank=True)),
                ("token", models.CharField(max_length=128, null=True, blank=True)),
                ("perms", models.CharField(max_length=32, null=True, blank=True)),
                ("last_sync", models.DateTimeField(null=True, blank=True)),
                ("user", models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["id"]},
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="JsonCache",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("flickr_id", models.CharField(max_length=50, null=True, blank=True)),
                ("info", models.TextField(null=True, blank=True)),
                ("sizes", models.TextField(null=True, blank=True)),
                ("exif", models.TextField(null=True, blank=True)),
                ("geo", models.TextField(null=True, blank=True)),
                ("exception", models.TextField(null=True, blank=True)),
                ("added", models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={},
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "flickr_id",
                    models.CharField(unique=True, max_length=50, db_index=True),
                ),
                ("show", models.BooleanField(default=True)),
                (
                    "last_sync",
                    models.DateTimeField(null=True, editable=False, blank=True),
                ),
                ("server", models.PositiveSmallIntegerField()),
                ("farm", models.PositiveSmallIntegerField()),
                ("secret", models.CharField(max_length=10)),
                ("originalsecret", models.CharField(max_length=10)),
                (
                    "originalformat",
                    models.CharField(max_length=4, null=True, blank=True),
                ),
                ("title", models.CharField(max_length=255, null=True, blank=True)),
                ("description", models.TextField(null=True, blank=True)),
                ("date_posted", models.DateTimeField(null=True, blank=True)),
                ("date_taken", models.DateTimeField(null=True, blank=True)),
                (
                    "date_taken_granularity",
                    models.PositiveSmallIntegerField(null=True, blank=True),
                ),
                ("date_updated", models.DateTimeField(null=True, blank=True)),
                ("url_page", models.URLField(max_length=255, null=True, blank=True)),
                ("slug", models.SlugField(max_length=255, null=True, blank=True)),
                ("exif", models.TextField(null=True, blank=True)),
                ("exif_camera", models.CharField(max_length=50, null=True, blank=True)),
                (
                    "exif_exposure",
                    models.CharField(max_length=10, null=True, blank=True),
                ),
                (
                    "exif_aperture",
                    models.CharField(max_length=10, null=True, blank=True),
                ),
                ("exif_iso", models.IntegerField(null=True, blank=True)),
                ("exif_focal", models.CharField(max_length=10, null=True, blank=True)),
                ("exif_flash", models.CharField(max_length=20, null=True, blank=True)),
                ("ispublic", models.NullBooleanField()),
                ("isfriend", models.NullBooleanField()),
                ("isfamily", models.NullBooleanField()),
                ("geo_latitude", models.FloatField(null=True, blank=True)),
                ("geo_longitude", models.FloatField(null=True, blank=True)),
                (
                    "geo_accuracy",
                    models.PositiveSmallIntegerField(null=True, blank=True),
                ),
                (
                    "license",
                    models.CharField(
                        default=0,
                        max_length=50,
                        choices=[
                            (b"0", b"All Rights Reserved"),
                            (b"1", b"Attribution-NonCommercial-ShareAlike License"),
                            (b"2", b"Attribution-NonCommercial License"),
                            (b"3", b"Attribution-NonCommercial-NoDerivs License"),
                            (b"4", b"Attribution License"),
                            (b"5", b"Attribution-ShareAlike License"),
                            (b"6", b"Attribution-NoDerivs License"),
                        ],
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        to="taggit.Tag",
                        through="taggit.TaggedItem",
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        verbose_name="Tags",
                    ),
                ),
                ("user", models.ForeignKey(to="flickr.FlickrUser")),
            ],
            options={
                "ordering": ("-date_posted", "-date_taken"),
                "get_latest_by": "date_posted",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="PhotoDownload",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("url", models.URLField(max_length=255, null=True, blank=True)),
                (
                    "image_file",
                    models.FileField(
                        null=True, upload_to=flickr.models.upload_path, blank=True
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        max_length=11,
                        choices=[
                            (b"large1600", b"Large 1600"),
                            (b"large", b"Large"),
                            (b"medium", b"Medium"),
                            (b"medium640", b"Medium 640"),
                            (b"largesquare", b"Large Square"),
                            (b"medium800", b"Medium 800"),
                            (b"small", b"Small"),
                            (b"thumb", b"Thumbnail"),
                            (b"square", b"Square"),
                            (b"small320", b"Small 320"),
                            (b"ori", b"Original"),
                            (b"large2048", b"Large 2048"),
                        ],
                    ),
                ),
                ("errors", models.TextField(null=True, blank=True)),
                (
                    "date_downloaded",
                    models.DateTimeField(auto_now=True, auto_now_add=True),
                ),
                ("photo", models.OneToOneField(to="flickr.Photo")),
            ],
            options={},
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="PhotoSet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "flickr_id",
                    models.CharField(unique=True, max_length=50, db_index=True),
                ),
                ("show", models.BooleanField(default=True)),
                (
                    "last_sync",
                    models.DateTimeField(null=True, editable=False, blank=True),
                ),
                ("server", models.PositiveSmallIntegerField()),
                ("farm", models.PositiveSmallIntegerField()),
                ("secret", models.CharField(max_length=10)),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(null=True, blank=True)),
                ("primary", models.CharField(max_length=50, null=True, blank=True)),
                ("date_posted", models.DateTimeField(null=True, blank=True)),
                ("date_updated", models.DateTimeField(null=True, blank=True)),
                (
                    "photos",
                    models.ManyToManyField(to="flickr.Photo", null=True, blank=True),
                ),
                ("user", models.ForeignKey(to="flickr.FlickrUser")),
            ],
            options={
                "ordering": ("-date_posted", "-id"),
                "get_latest_by": "date_posted",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="PhotoSizeData",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        max_length=11,
                        choices=[
                            (b"large1600", b"Large 1600"),
                            (b"large", b"Large"),
                            (b"medium", b"Medium"),
                            (b"medium640", b"Medium 640"),
                            (b"largesquare", b"Large Square"),
                            (b"medium800", b"Medium 800"),
                            (b"small", b"Small"),
                            (b"thumb", b"Thumbnail"),
                            (b"square", b"Square"),
                            (b"small320", b"Small 320"),
                            (b"ori", b"Original"),
                            (b"large2048", b"Large 2048"),
                        ],
                    ),
                ),
                ("width", models.PositiveIntegerField(null=True, blank=True)),
                ("height", models.PositiveIntegerField(null=True, blank=True)),
                ("source", models.URLField(null=True, blank=True)),
                ("url", models.URLField(null=True, blank=True)),
                ("photo", models.ForeignKey(related_name="sizes", to="flickr.Photo")),
            ],
            options={},
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name="photosizedata", unique_together=set([("photo", "size")])
        ),
        migrations.AddField(
            model_name="collection",
            name="sets",
            field=models.ManyToManyField(to="flickr.PhotoSet", null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="collection",
            name="user",
            field=models.ForeignKey(to="flickr.FlickrUser"),
            preserve_default=True,
        ),
    ]
