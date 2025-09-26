from django.contrib import admin
from .models import *


admin.site.register(Employee)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id','title','uploaded_at')