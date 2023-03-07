from django.contrib import admin
from webapp.models import Task, Type, Status

# Register your models here.

admin.site.register(Task)
admin.site.register(Type)
admin.site.register(Status)