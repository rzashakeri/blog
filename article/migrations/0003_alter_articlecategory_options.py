# Generated by Django 4.0.4 on 2022-04-28 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_articlecategory_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]