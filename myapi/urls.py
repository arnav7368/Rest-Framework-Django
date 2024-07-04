from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

def home(request):
    return HttpResponse ("Welcome to my Page")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("myapp/a1/",include("myapp.urls")),
    path("",home)
]
