# Generated by Django 4.0.4 on 2022-04-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('link', models.URLField(verbose_name='link')),
            ],
            options={
                'verbose_name': 'header link',
                'verbose_name_plural': 'header Links',
            },
        ),
    ]