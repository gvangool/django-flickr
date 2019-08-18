#!/usr/bin/env python
# encoding: utf-8
import datetime

from django import template

register = template.Library()


@register.inclusion_tag("flickr/photo.html")
def flickr_photo(photo, size="medium", flickr_link=False):
    if not photo:
        return {}
    if size == "large" and photo.date_posted.date() <= datetime.date(2010, 5, 25):
        if photo.user.ispro:
            size = "ori"
        else:
            size = "medium640"
    return {
        "photo": photo,
        "size": size,
        "flickr_link": flickr_link,
        "photo_size": getattr(photo, size),
    }
