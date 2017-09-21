from drf_haystack.serializers import HaystackSerializer

from apps.categories.search_indexes import CategoryIndex
from apps.categories.serializers import CategorySearchSerializer
from apps.users.search_indexes import UserIndex
from apps.users.serializers import UserSearchSerializer


class GlobalSearchSerializer(HaystackSerializer):

    class Meta:
        field_aliases = {
            "q": "autocomplete",
        }
        index_classes = [UserIndex, CategoryIndex]
        serializers = {
            UserIndex: UserSearchSerializer,
            CategoryIndex: CategorySearchSerializer,
        }
