# Generated by Django 4.0.4 on 2022-04-30 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_us',
            field=models.CharField(default='test', max_length=300, verbose_name='about us'),
            preserve_default=False,
        ),
    ]