from django.contrib import admin
from django.urls import path

from .views.base import IndexView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index')
]