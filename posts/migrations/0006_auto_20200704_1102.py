# Generated by Django 3.0.4 on 2020-07-04 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200703_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='bio',
            new_name='about',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='name_a',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='last_name',
            new_name='name_b',
        ),
    ]
