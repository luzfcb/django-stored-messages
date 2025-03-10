from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required

from .serializers import InboxSerializer
from .backends.exceptions import MessageDoesNotExist


class InboxViewSet(viewsets.ViewSet):
    """
    Provides `list` and `detail` actions, plus a `read` POST endpoint for
    marking inbox messages as read.
    """

    def list(self, request):
        from .settings import stored_messages_settings
        backend = stored_messages_settings.STORAGE_BACKEND()
        messages = backend.inbox_list(request.user)
        serializer = InboxSerializer(messages, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        from .settings import stored_messages_settings
        backend = stored_messages_settings.STORAGE_BACKEND()

        try:
            msg = backend.inbox_get(request.user, pk)
        except MessageDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InboxSerializer(msg, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def read(self, request, pk=None):
        """
        Mark the message as read (i.e. delete from inbox)
        """
        from .settings import stored_messages_settings
        backend = stored_messages_settings.STORAGE_BACKEND()

        try:
            backend.inbox_delete(request.user, pk)
        except MessageDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response({'status': 'message marked as read'})


@login_required
@api_view(['POST'])
def mark_all_read(request):
    """
    Mark all messages as read (i.e. delete from inbox) for current logged in user
    """
    from .settings import stored_messages_settings
    backend = stored_messages_settings.STORAGE_BACKEND()
    backend.inbox_purge(request.user)
    return Response({"message": "All messages read"})
