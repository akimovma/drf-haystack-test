from rest_framework import serializers

from .models import Category
from drf_haystack.serializers import HaystackSerializer
from .search_indexes import CategoryIndex


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'name', 'description')
        read_only_fields = ('id',)


class CategorySearchSerializer(HaystackSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:category-detail")
    content_type = serializers.CharField(source='model_name')

    class Meta:
        index_classes = [CategoryIndex]
        fields = ['name', 'title', 'url', 'content_type', 'autocomplete']
        ignore_fields = ["autocomplete"]
