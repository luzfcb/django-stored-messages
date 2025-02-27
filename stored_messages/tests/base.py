from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from importlib import reload

from unittest import mock

from stored_messages import storage
from stored_messages import settings


class BaseTest(TestCase):
    def setUp(self):
        # settings and storage modules should be reloaded
        reload(settings)
        reload(storage)

        self.factory = RequestFactory()
        self.user = get_user_model().objects.create_user("test_user", "t@user.com", "123456")
        self.request = RequestFactory().get('/')
        self.request.session = mock.MagicMock()
        self.request.user = self.user

    def tearDown(self):
        self.user.delete()


class BackendBaseTest(BaseTest):
    """
    Tests that need to access a Backend.
    Given the dynamic nature of Stored Messages settings, retrieving the backend class when we
    need to ovveride settings is a little bit tricky
    """

    def setUp(self):
        super().setUp()
        self.backend = settings.stored_messages_settings.STORAGE_BACKEND()

    def tearDown(self):
        self.backend._flush()
