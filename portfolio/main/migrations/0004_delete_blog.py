# Generated by Django 4.2.3 on 2024-05-31 05:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_rename_article_blog"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Blog",
        ),
    ]
