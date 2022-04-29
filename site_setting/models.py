from django.db import models


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, verbose_name='site name')
    site_url = models.URLField(max_length=300, verbose_name='site url')
    site_logo = models.ImageField(upload_to='logo/', verbose_name=' site logo')
    about_us = models.CharField(max_length=400, verbose_name='about us')
    email = models.EmailField(verbose_name='site email')
    phone_number = models.CharField(max_length=100, verbose_name='mobile number')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'site setting'
        verbose_name_plural = 'site settings'


class HeaderLink(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    url = models.URLField(verbose_name='link')
    is_active = models.BooleanField(verbose_name='is active ?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'header link'
        verbose_name_plural = 'header Links'