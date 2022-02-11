# Generated by Django 4.0 on 2021-12-31 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishapp', '0002_remove_fish_category_remove_fish_catgy_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='pfish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=200, null=True)),
                ('cate', models.CharField(max_length=200, null=True)),
                ('weight', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('img', models.ImageField(null=True, upload_to='image')),
            ],
        ),
    ]