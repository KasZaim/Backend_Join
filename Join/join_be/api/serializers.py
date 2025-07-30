from rest_framework import serializers
from user_auth_app.api.serializers import UserProfileSerializer
from join_be.models import Contacts,Tasks
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

class ContactsSerializer(serializers.ModelSerializer):
    contact_link = serializers.SerializerMethodField()
    class Meta:
        model = Contacts
        fields = ['id', 'firstname','lastname', 'mail', 'phone', 'initials', 'color','contact_link']
        extra_kwargs = {
            'user': {'read_only': True}  # Das Feld `user` ist schreibgeschützt und wird automatisch gesetzt
        }

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)
    
    def get_contact_link(self, obj):
        request = self.context.get('request')
        return reverse('contacts-detail', kwargs={'pk': obj.pk}, request=request)


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source='userprofile', read_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
       model = User
       fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile','password']


class TasksSerializer(serializers.ModelSerializer):
    task_link = serializers.SerializerMethodField()
    class Meta:
        model = Tasks
        fields = ['id','category', 'topic', 'headline', 'description', 'clients', 'prio', 'date', 'subtasks','task_link']
    
    def get_subtasks(self, obj):
        subtasks = obj.subtasks.all()
        return TasksSerializer(subtasks, many=True).data
    
    def get_task_link(self, obj):
        request = self.context.get('request')
        return reverse('tasks-detail', kwargs={'pk': obj.pk}, request=request)
