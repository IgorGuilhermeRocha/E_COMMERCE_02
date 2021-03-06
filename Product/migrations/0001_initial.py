# Generated by Django 4.0.3 on 2022-03-16 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/%Y/%m')),
                ('slug', models.SlugField(unique=True)),
                ('original_price', models.FloatField()),
                ('promotional_price', models.FloatField(default=0)),
            ],
        ),
    ]
