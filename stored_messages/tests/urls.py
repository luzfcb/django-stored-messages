from django.conf.urls import include

from stored_messages.tests.views import message_view, message_create, message_create_mixed
from django.urls import path

urlpatterns = [
    path('consume', message_view),
    path('create', message_create),
    path('create_mixed', message_create_mixed),
    path('messages', include(('stored_messages.urls', 'reviews'), namespace='stored_messages'))
]
