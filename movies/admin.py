from django.contrib import admin

from .models import Studio, Director, Movies

admin.site.register(Studio)
admin.site.register(Director)
admin.site.register(Movies)
