# Generated by Django 3.1.3 on 2021-01-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0002_remove_userprofile_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='telephone',
            field=models.CharField(blank=True, default=None, max_length=35, null=True),
        ),
    ]