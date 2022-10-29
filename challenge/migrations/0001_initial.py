# Generated by Django 3.0.3 on 2020-09-28 19:00

import datetime
from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sequence', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('geometry', models.TextField(default='')),
                ('multipolygon', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('is_published', models.BooleanField(default=True)),
                ('zoom', models.FloatField(default=5)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('camera_make', models.ManyToManyField(to='sequence.CameraMake')),
                ('transport_type', models.ManyToManyField(to='sequence.TransType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]