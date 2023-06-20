from django.db import models

# Create your models here.
from shortener.models import stored_url

class ClickEventManager(models.Manager):
    def create_event(self,urlinstance):
        if isinstance(urlinstance,stored_url):
            obj,created = self.get_or_create(st_url = urlinstance)
            obj.count+=1 
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    st_url = models.OneToOneField(stored_url,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()
    
    def __str__(self):
        return "{i}".format(i=self.count)
