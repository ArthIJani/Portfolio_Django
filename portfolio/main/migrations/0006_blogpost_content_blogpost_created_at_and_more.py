# Generated by Django 4.2.3 on 2024-06-01 07:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_blogpost"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="content",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="blogpost",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="blogpost",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
