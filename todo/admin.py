from django.contrib import admin

from .models import Todo,Tag

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','content','creator',)
    list_filter = ('status',)
    search_fields = ('title','creator__username')

admin.site.register(Todo,TodoAdmin)
admin.site.register(Tag)
