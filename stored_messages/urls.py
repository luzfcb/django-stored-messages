"""
At the moment this module does something only when restframework is available
"""
from django.conf import settings
from django.urls import path

if 'rest_framework' in settings.INSTALLED_APPS:
    from rest_framework.routers import DefaultRouter
    from django.conf.urls import include
    from . import views

    router = DefaultRouter()
    router.register(r'inbox', views.InboxViewSet, basename='inbox')

    urlpatterns = [
        path('', include(router.urls)),
        path('mark_all_read/', views.mark_all_read, name='mark_all_read'),
    ]
