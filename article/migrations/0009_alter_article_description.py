# Generated by Django 4.0.4 on 2022-04-29 23:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_alter_articlecategory_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]