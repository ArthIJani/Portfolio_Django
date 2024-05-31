# Generated by Django 4.2.3 on 2024-05-31 09:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_delete_blog"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
            ],
        ),
    ]
