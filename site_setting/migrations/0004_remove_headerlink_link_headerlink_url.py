# Generated by Django 4.0.4 on 2022-04-29 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0003_headerlink_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headerlink',
            name='link',
        ),
        migrations.AddField(
            model_name='headerlink',
            name='url',
            field=models.URLField(default='false', verbose_name='url'),
            preserve_default=False,
        ),
    ]
