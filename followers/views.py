from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from followers.models import Follower
from followers.serializers import FollowerSerializer

class FollowerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
        
class FollowerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()