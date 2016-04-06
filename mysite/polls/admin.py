from django.contrib import admin

# Register your models here.

from .models import Question

# this allows the admin page to have access to the Question model 
admin.site.register(Question)