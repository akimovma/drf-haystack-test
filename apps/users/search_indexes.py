from haystack import indexes
from .models import User


class UserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    username = indexes.CharField(model_attr="username")
    first_name = indexes.CharField(model_attr="first_name")
    last_name = indexes.CharField(model_attr="last_name")

    autocomplete = indexes.EdgeNgramField(model_attr='username')

    @staticmethod
    def prepare_autocomplete(obj):
        return " ".join((obj.username, obj.first_name, obj.last_name))

    def get_model(self):
        return User
