from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.http import Http404, HttpResponse,HttpResponseRedirect
from .models import stored_url,feedback
from .forms import SubmitUrlForm,SubmitFeedbackForm
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
            "title": "Shorten a long link",
        }
        return render(request,"shortener/home.html",context)
    
    def post(self,request,*args, **kwargs):
        form = SubmitUrlForm(request.POST)
        template = "shortener/home.html"
        context = {
            "form" : form,
            "title" : "Shorten a long link"
        }
        objs = ClickEvent.objects.all()
        if form.is_valid():
            submitted_url = form.cleaned_data.get("url")
            # print(submitted_url)
            if not "https://" in submitted_url:
                submitted_url = "https://" + submitted_url
            obj,created = stored_url.objects.get_or_create(url = submitted_url)
            context = {
                "object": obj,
                "created": created,
                "count" : objs.count,
                # "time":objs.st_url
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already_exists.html"
        
        return render(request,template,context)

class About_view(View):
    def get(self,request,*args, **kwargs):
        context = {
            "name": "Md. Rejoanur Rahman Apu",
        }
        return render(request,"shortener/about.html",context)

class Services_view(View):
    def get(self,request,*args, **kwargs):
        context = {
            "dummy": "Nothing",
        }
        return render(request,"shortener/services.html",context)

class Contact_View(View):
    def get(self,request,*args, **kwargs):
        form = SubmitFeedbackForm()
        context = {
            "gmail" : "rejoan523@gmail.com",
            "form":form
        }
        return render(request,"shortener/contact.html",context) 
    
    def post(self,request,*args, **kwargs):
        form = SubmitFeedbackForm(request.POST)
        context = {
        }
        if form.is_valid:
            form.save()
            context = {
                "form":form,
                "gmail" : "rejoan523@gmail.com",
            }
            return redirect('../contact')
        
        return render(request,"shortener/contact.html",context)

class class_redirect_views(View):
    def get(self,request,short_url=None,*args, **kwargs):
        # print(short_url)
        qs = stored_url.objects.filter(short_url__iexact = short_url)
        # print(short_url)
        if qs.count() !=1 and not qs.exists():
            # print(2)
            raise Http404
        obj = qs.first()
        #click events
        ClickEvent.objects.create_event(obj)
        return HttpResponseRedirect(obj.url)

    # def post(self,request,shortcode=None,*args,**kwargs):
    #     return HttpResponse()