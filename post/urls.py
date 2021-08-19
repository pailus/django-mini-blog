from .views import *
from django.urls import path, include
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'post', PostViewset)
router.register(r'comment', CommentViewset)



urlpatterns = [
    path('api/', include(router.urls)),
]



