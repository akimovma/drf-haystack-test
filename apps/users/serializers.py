from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer

from .models import User
from .search_indexes import UserIndex


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'is_active', 'first_name', 'last_name',
                  'downloads_laptop', 'downloads_apple', 'downloads_android', 'date_joined',
                  'photo')
        read_only_fields = ('id', 'date_joined', 'is_active')


class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        write_only_fields = ('password',)


class UserSearchSerializer(HaystackSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")
    content_type = serializers.CharField(source='model_name')

    class Meta:
        index_classes = [UserIndex]
        fields = [
            "username", "first_name", "last_name", "url", "content_type", "autocomplete"
        ]
        ignore_fields = ["autocomplete"]

