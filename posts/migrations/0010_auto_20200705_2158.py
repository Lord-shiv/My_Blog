# Generated by Django 3.0.4 on 2020-07-05 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20200705_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='Profession',
        ),
        migrations.RemoveField(
            model_name='author',
            name='about',
        ),
        migrations.RemoveField(
            model_name='author',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='author',
            name='name_a',
        ),
        migrations.RemoveField(
            model_name='author',
            name='name_b',
        ),
        migrations.RemoveField(
            model_name='author',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='author',
            name='profile_picture',
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('name_a', models.CharField(max_length=200, null=True)),
                ('name_b', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Profession', models.CharField(max_length=200, null=True)),
                ('about', models.CharField(max_length=1000, null=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.Author')),
            ],
        ),
    ]
