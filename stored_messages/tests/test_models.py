from .base import BaseTest

from django.utils.timezone import now, timedelta
from django.contrib.messages.storage import default_storage

from stored_messages import add_message, STORED_ERROR
from stored_messages.models import MessageArchive, Inbox


class TestInbox(BaseTest):
    def test_expire(self):
        self.request._messages = default_storage(self.request)
        add_message(self.request, STORED_ERROR, "an SOS to the world ☢")
        mas = MessageArchive.objects.all()
        self.assertEqual(len(mas), 1)
        ma = mas[0]
        ma.message.date = now() - timedelta(days=365)
        ma.message.save()
        inbox = Inbox.objects.create(user=ma.user, message=ma.message)
        self.assertTrue(inbox.expired())
