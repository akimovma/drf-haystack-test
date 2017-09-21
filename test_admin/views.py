from drf_haystack.mixins import MoreLikeThisMixin
from drf_haystack.viewsets import HaystackViewSet
from drf_haystack.filters import HaystackFilter, HaystackAutocompleteFilter

from .serializers import GlobalSearchSerializer


class GlobalSearchViewSet(MoreLikeThisMixin, HaystackViewSet):
    serializer_class = GlobalSearchSerializer
    filter_backends = [HaystackAutocompleteFilter, HaystackFilter]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        grouped_results = dict()
        if response.data:
            for result_item in response.data:
                grouped_results.setdefault(result_item['content_type'], []).append(result_item)
        response.data = grouped_results
        return response
