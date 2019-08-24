from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from flickr.views import (
    IndexView,
    PhotoSetView,
    auth,
    method_call,
    oauth,
    oauth_access,
    photo,
)

urlpatterns = [
    url(r"^auth/$", oauth, name="flickr_auth"),
    url(r"^auth/complete/$", oauth_access, name="flickr_complete"),
    url(r"^flickr-callback/$", auth, name="flickr_auth_callback"),
    url(r"^method/(?P<method>.*)/$", method_call, name="flickr_method"),
    url(r"^set/(?P<flickr_id>.*)/$", PhotoSetView.as_view(), name="flickr_photoset"),
    url(r"^photo/(?P<flickr_id>.*)/$", photo, name="flickr_photo"),
    url(r"^$", IndexView.as_view(), name="flickr_index"),
]
