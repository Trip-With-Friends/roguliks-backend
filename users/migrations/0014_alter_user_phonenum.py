# Generated by Django 4.0.3 on 2022-10-28 10:00

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_user_allow_politics_and_processing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phonenum',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
