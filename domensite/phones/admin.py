from django.contrib import admin

from .models import *

class PhonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')

admin.site.register(Phones, PhonesAdmin)
admin.site.register(Category)