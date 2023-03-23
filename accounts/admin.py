from django.contrib import admin

from .models import  *
admin.site.register(Investor) 
admin.site.register(Project) 
admin.site.register(Investment) 
admin.site.register(Tag) 