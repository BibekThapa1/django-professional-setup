from .views import BlogViewset

from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('blog', BlogViewset, basename='blog')

urlpatterns = [
    path('', include(router.urls))
]