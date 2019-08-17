from django.conf.urls import patterns, url

from flickr.views import IndexView, PhotoSetView

urlpatterns = patterns('',
    url(r'^auth/$', "flickr.views.oauth", name="flickr_auth"),
    url(r'^auth/complete/$', "flickr.views.oauth_access", name="flickr_complete"),

    url(r'^auth/deprecated/$', "flickr.views.auth", name="flickr_auth_deprecated"),
    url(r'^flickr-callback/$', "flickr.views.auth", name="flickr_auth_callback"),

    url(r'^method/(?P<method>.*)/$', "flickr.views.method_call", name="flickr_method"),
    url(r'^set/(?P<flickr_id>.*)/$', PhotoSetView.as_view(), name="flickr_photoset"),
    url(r'^photo/(?P<flickr_id>.*)/$', "flickr.views.photo", name="flickr_photo"),
    url(r'^$', IndexView.as_view(), name="flickr_index"),
)
