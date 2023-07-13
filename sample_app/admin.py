from django.contrib import admin
from .models import Content
# Register your models here.

class AdminContent(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(Content,AdminContent)