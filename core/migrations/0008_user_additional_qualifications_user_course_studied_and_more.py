# Generated by Django 4.0.5 on 2022-07-22 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_event_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='additional_qualifications',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='course_studied',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='present_position_held',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='special_contribution',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='year_of_passing',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.RemoveField(
            model_name='user',
            name='i_am',
        ),
        migrations.AddField(
            model_name='user',
            name='i_am',
            field=models.ManyToManyField(to='core.group'),
        ),
    ]
