from django.urls import path, include
from rest_framework import routers
from .views import StudentViewsets

router=routers.DefaultRouter()
router.register(r"students",StudentViewsets)

urlpatterns = [
    path("",include(router.urls))
]
