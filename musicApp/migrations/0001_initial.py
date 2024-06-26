# Generated by Django 5.0.6 on 2024-05-27 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('artist', models.CharField(blank=True, max_length=150)),
                ('album', models.CharField(blank=True, max_length=150)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('playlists', models.ManyToManyField(blank=True, related_name='songs', to='musicApp.playlist')),
                ('tags', models.ManyToManyField(blank=True, related_name='songs', to='musicApp.tag')),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='playlists', to='musicApp.tag'),
        ),
    ]
