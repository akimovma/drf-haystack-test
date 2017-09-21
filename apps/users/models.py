from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    photo = models.FileField(upload_to='profile_avatars')

    downloads_laptop = models.IntegerField(default=0)
    downloads_apple = models.IntegerField(default=0)
    downloads_android = models.IntegerField(default=0)

    email = models.EmailField(_('email address'),
                              blank=True,
                              error_messages={
                                  'unique': _("A user with that email already exists."),
                              },
                              unique=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
