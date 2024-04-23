# Generated by Django 2.2.6 on 2020-02-22 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='products_images/')),
                ('category', models.CharField(choices=[('M', 'mobile'), ('T', 'tv'), ('G', 'grocery')], max_length=30)),
                ('tags', models.ManyToManyField(to='product.Tags')),
            ],
        ),
    ]