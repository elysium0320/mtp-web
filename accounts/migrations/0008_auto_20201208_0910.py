# Generated by Django 3.0.3 on 2020-12-08 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_custombanner_linked_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='hall_link',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='hall_text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='is_hall',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='grade',
            name='is_hall_avatar',
            field=models.BooleanField(default=False),
        ),
    ]
