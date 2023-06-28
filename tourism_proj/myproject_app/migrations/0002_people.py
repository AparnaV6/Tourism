# Generated by Django 4.1.7 on 2023-03-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myproject_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="People",
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
                ("name", models.CharField(max_length=250)),
                ("img", models.ImageField(upload_to="pics")),
                ("desc", models.TextField()),
            ],
        ),
    ]
