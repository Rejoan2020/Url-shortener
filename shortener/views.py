from django.shortcuts import render,get_object_or_404
from django.views import View
from django.http import Http404, HttpResponse,HttpResponseRedirect
from .models import stored_url
from .forms import SubmitUrlForm
from analytics.models import ClickEvent

# Create your views here.
# def func_redirect_views(request,shortcode=None,*args, **kwargs):
    # print(kwargs)
    # outobj = None
    # obj = stored_url.objects.filter(short_url=shortcode)
    # if obj.exists() and obj.count()==1:
    #     outobj = obj.first().url
    # obj = get_object_or_404(stored_url, short_url = shortcode)
    
    # return HttpResponseRedirect(obj.url)

class home_view(View):
    def get(self,request,*args, **kwargs):
        form = SubmitUrlForm()
        context = {
            "form": form,
            "title": "Cutly.com"
        }
        return render(request,"shortener/home.html",context)
    
    def post(self,request,*args, **kwargs):
        form = SubmitUrlForm(request.POST)
        template = "shortener/home.html"
        context = {
            "form" : form,
            "title" : "Shorten your long urls"
        }
        if form.is_valid():
            submitted_url = form.cleaned_data.get("url")
            if not "https://" in submitted_url:
                submitted_url = "https://" + submitted_url
            obj,created = stored_url.objects.get_or_create(url = submitted_url)
            context = {
                "object": obj,
                "created": created
            }
            # print(obj)
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already_exists.html"
        
        return render(request,template,context)

class class_redirect_views(View):
    def get(self,request,short_url=None,*args, **kwargs):
        # print(short_url)
        qs = stored_url.objects.filter(short_url__iexact = short_url)
        print(short_url)
        if qs.count() !=1 and not qs.exists():
            # print(2)
            raise Http404
        obj = qs.first()
        #click events
        print(obj)
        ClickEvent.objects.create_event(obj)
        return HttpResponseRedirect(obj.url)

    # def post(self,request,shortcode=None,*args,**kwargs):
    #     return HttpResponse()