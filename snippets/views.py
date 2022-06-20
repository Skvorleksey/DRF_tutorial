from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly



class UserList(generics.ListAPIView):
    """List all users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """Retrieve user info"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetList(generics.ListCreateAPIView):
    """List all snippets, or create a new snippet."""
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a code snippet."""
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
