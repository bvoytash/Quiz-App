# Generated by Django 4.0.1 on 2022-03-03 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore_auth', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
