from django.contrib import admin

from .models import Topic, Entry#, Entry_2

admin.site.register(Topic)
admin.site.register(Entry)
# admin.site.register(Entry_2)