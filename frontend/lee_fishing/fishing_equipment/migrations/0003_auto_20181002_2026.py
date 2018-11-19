# Generated by Django 2.0.8 on 2018-10-02 20:26

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fishing_equipment', '0002_auto_20181002_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='smaller_picture',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='product_thumbs'),
        ),
    ]
