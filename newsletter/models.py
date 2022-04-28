from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'
