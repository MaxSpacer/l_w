# Generated by Django 2.1.4 on 2019-01-12 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0002_auto_20190112_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribers',
            old_name='subscribers_email',
            new_name='subscriber_email',
        ),
        migrations.RenameField(
            model_name='subscribers',
            old_name='subscribers_name',
            new_name='subscriber_name',
        ),
        migrations.RenameField(
            model_name='subscribers',
            old_name='subscribers_phone',
            new_name='subscriber_phone',
        ),
    ]
