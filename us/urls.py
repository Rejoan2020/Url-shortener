"""
URL configuration for us project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from shortener.views import class_redirect_views,home_view,Contact_View,About_view,Services_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',About_view.as_view()),
    path('services/',Services_view.as_view()),
    path('contact/',Contact_View.as_view()),
    re_path(r'^(?P<short_url>[\w{6,15}]+)/$', class_redirect_views.as_view(),name = "sc"),
    # re_path(r'^b/(?P<shortcode>[\w{6,15}]+)/$', func_redirect_views),
    path('',home_view.as_view()),
]
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)