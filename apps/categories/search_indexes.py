from django.utils import timezone
from haystack import indexes
from .models import Category


class CategoryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr="name")
    title = indexes.CharField(model_attr="title")

    autocomplete = indexes.EdgeNgramField()

    @staticmethod
    def prepare_autocomplete(obj):
        return " ".join((obj.name, obj.title,))

    def get_model(self):
        return Category
