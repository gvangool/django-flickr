import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from munch import munchify

from flickr.api import FlickrApi
from flickr.models import FlickrUser, Photo, PhotoSet
from flickr.shortcuts import get_token_for_user

FLICKR_KEY = getattr(settings, "FLICKR_KEY", None)
FLICKR_SECRET = getattr(settings, "FLICKR_SECRET", None)
PERMS = getattr(settings, "FLICKR_PERMS", None)


@login_required
def oauth(request):
    token = get_token_for_user(request.user)
    if not token:
        api = FlickrApi(FLICKR_KEY, FLICKR_SECRET)
        url = api.auth_url(
            request,
            perms=PERMS,
            callback=request.build_absolute_uri(reverse("flickr_complete")),
        )
        return HttpResponseRedirect(url)
    else:
        api = FlickrApi(FLICKR_KEY, FLICKR_SECRET, token, fallback=False)
        try:
            data = api.get("flickr.test.login")
        except:  # # FlickrUnauthorizedCall:
            fs = FlickrUser.objects.get(user=request.user)
            fs.token = None
            fs.perms = None
            fs.save()
            return HttpResponseRedirect(reverse("flickr_auth"))
    return render(request, "flickr/auth_ok.html", {"token": token})


@login_required
def oauth_access(request):
    api = FlickrApi(FLICKR_KEY, FLICKR_SECRET)
    data = api.access_token(request)
    if data:
        data = munchify(data)
        fs, created = FlickrUser.objects.get_or_create(user=request.user)
        fs.token = data.token
        fs.nsid = data.oauth.user.nsid
        fs.username = data.oauth.user.username
        fs.full_name = data.oauth.user.fullname
        fs.perms = data.oauth.perms._content
        fs.save()
        return HttpResponseRedirect(reverse("flickr_auth"))
    raise Exception("Ups! No data...")


@login_required
def auth(request):
    from flickr.api import FlickrAuthApi

    api = FlickrAuthApi(FLICKR_KEY, FLICKR_SECRET)
    token = get_token_for_user(request.user)
    if not token:
        try:
            fs = FlickrUser.objects.get(user=request.user)
            token = fs.token
        except FlickrUser.DoesNotExist:
            auth_url = api.auth_url(PERMS)
            return render(request, "flickr/auth.html", {"auth_url": auth_url})
    else:
        fs = FlickrUser.objects.get(user=request.user)
    return render(request, "flickr/auth_ok.html", {"token": fs.token})


class IndexView(ListView):
    template_name = "flickr/index.html"
    paginate_by = 10
    context_object_name = "photo_list"

    def get_queryset(self):
        return Photo.objects.public()

    def get_context_data(self, **kwargs):
        context_data = super(IndexView, self).get_context_data(**kwargs)
        context_data["photosets"] = PhotoSet.objects.all()
        return context_data


class PhotoSetView(IndexView):
    def get_queryset(self):
        return Photo.objects.public(photoset__flickr_id__in=[self.kwargs["flickr_id"]])

    def get_context_data(self, **kwargs):
        context_data = super(PhotoSetView, self).get_context_data(**kwargs)
        context_data["photoset"] = get_object_or_404(
            PhotoSet, flickr_id=self.kwargs["flickr_id"]
        )
        return context_data


def photo(request, flickr_id):
    try:
        photo = Photo.objects.get(flickr_id=flickr_id)
    except Photo.DoesNotExist:
        photo = get_object_or_404(Photo, pk=flickr_id)
    return render(request, "flickr/photo_page.html", {"photo": photo})


def method_call(request, method):
    api = FlickrApi(FLICKR_KEY, FLICKR_SECRET)
    if request.user.is_authenticated():
        api.token = get_token_for_user(request.user)
        auth = True
    else:
        auth = False
    data = api.get(method, auth=auth, photo_id="6110054503")
    return HttpResponse(json.dumps(data))
