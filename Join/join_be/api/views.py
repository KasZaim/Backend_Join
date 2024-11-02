from rest_framework.response import Response
from .serializers import UserSerializer, ContactsSerializer, TasksSerializer
from rest_framework import mixins, generics, viewsets
from rest_framework.decorators import action
from join_be.models import Contacts,Tasks
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet): #ModelViewSet
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=True, methods=['get'])
    def contacts(self, request, pk=None):
        user = self.get_object()
        contacts = Contacts.objects.filter(user=user)
        serializer = ContactsSerializer(contacts, many=True)
        return Response(serializer.data)

class ContactsViewSet(viewsets.ModelViewSet): #ModelViewSet
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Nur Kontakte des angemeldeten Benutzers abrufen
        user = self.request.user
        return Contacts.objects.filter(user=user)
    
class TasksViewSet(viewsets.ModelViewSet): #ModelViewSet
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer