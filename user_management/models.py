from django.db import models
from django.contrib.auth.models import AbstractUser


# customize user model
class User(AbstractUser):
    mobile = models.CharField(max_length=100, null=True, blank=True, verbose_name='mobile')
    avatar = models.ImageField(upload_to='avatars/')
    email_active_code = models.CharField(max_length=300, verbose_name='activation code')

    def __str__(self):
        if self.first_name != '' and self.last_name != '':
            return self.get_full_name()
        return self.email

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
