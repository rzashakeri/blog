# Generated by Django 4.0.4 on 2022-04-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0002_headerlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerlink',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is active ?'),
            preserve_default=False,
        ),
    ]