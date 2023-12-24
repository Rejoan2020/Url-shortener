from django.contrib import admin

# Register your models here.
from .models import stored_url,feedback

admin.site.register(stored_url)
admin.site.register(feedback)