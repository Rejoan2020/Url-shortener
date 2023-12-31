from django.db import models
from .utils import short_url_generator,removewww
from django.conf import settings
# Create your models here.
from .validators import validate_dot_com,validate_url,email_validator
from django_hosts.resolvers import reverse

class stored_urlManager(models.Manager):
    def all(self,*args,**kwargs):
        querey_set = super(stored_urlManager, self).all(*args,**kwargs)
        active_qs = querey_set.filter(active=True)
        return active_qs
    
    def refresh_short_urls(self,itm=None):
        query_set = stored_url.objects.filter(id__gte=1)
        refreshed_slugs = 0
        if itm is not None and isinstance(itm,int):
            query_set = query_set.order_by('-id')[:itm]
        for query in query_set:
            query.short_url = short_url_generator(query)
            print(query.id)
            query.save()
            refreshed_slugs+=1
        return  "number of refreshed short_urls {x}".format(x = refreshed_slugs)

SHORTCODE_MAX = getattr(settings,"MAX_SIZE",15)

class stored_url(models.Model):
    url = models.CharField(max_length=10000, validators=[validate_url,validate_dot_com])
    short_url = models.CharField(max_length=SHORTCODE_MAX,unique=True,blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def save(self,*args, **kwargs):
        # print("hi")
        if self.short_url is None or self.short_url == "":
            self.short_url = short_url_generator(self)
        super(stored_url,self).save(*args,**kwargs)

    objects = stored_urlManager()
    # object.all()

    def __str__(self):
        return str(self.url)
    
    def __unicode__(self):
        return str(self.url)
    
    def get_short_url(self):
        self.save()
        path = reverse('sc',kwargs={'short_url':self.short_url},scheme='http')
        # print(path)
        path = removewww(path)
        return path

class feedback(models.Model):
    name = models.CharField(max_length = 50,)
    email = models.EmailField(max_length = 60,validators = [email_validator])
    message = models.TextField(max_length = 1000)

    def save(self,*args, **kwargs):
        print('saving...')
        super(feedback,self).save(*args,**kwargs)
    
    def __str__(self):
        self.save()
        ret_str = self.message + " (" + self.name + ")"
        return str(ret_str) 
    def __unicode__(self):
        ret_str = self.message + " (" + self.name + ")"
        return str(ret_str)