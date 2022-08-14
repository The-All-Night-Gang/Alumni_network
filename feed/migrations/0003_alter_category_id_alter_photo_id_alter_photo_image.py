# Generated by Django 4.0.5 on 2022-07-19 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_alter_category_id_alter_photo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='photo'),
        ),
    ]
