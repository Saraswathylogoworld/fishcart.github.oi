# Generated by Django 4.0 on 2021-12-31 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishapp', '0003_pfish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
