from .views import *
from django.urls import path, include
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'category', CategoryViewset)
router.register(r'tag', TagViewset)



urlpatterns = [
    path('api/', include(router.urls)),
]
