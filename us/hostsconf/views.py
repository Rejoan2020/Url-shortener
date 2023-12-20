from django.conf import settings
from django.http import HttpResponseRedirect

DEFAULT_REDIRECT_PATH = getattr(settings,'DEFAULT_REDIRECT_PATH','http://url-shortener-ashy-two.vercel.app')

def wildcard_redirect(request,path=None):
    new_url = DEFAULT_REDIRECT_PATH
    if path is not None:
        new_url = DEFAULT_REDIRECT_PATH + "/" + path
    return HttpResponseRedirect(new_url)