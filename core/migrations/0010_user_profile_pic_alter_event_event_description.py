# Generated by Django 4.0.5 on 2022-07-24 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_user_i_am_user_i_am'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='person.svg', upload_to='profile_pic'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
