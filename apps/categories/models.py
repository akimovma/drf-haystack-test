from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from apps.users.models import User


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    title = models.CharField(_('Title'), max_length=100)
    description = models.CharField(_('Description'), max_length=300)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return 'Category - %s' % self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)

