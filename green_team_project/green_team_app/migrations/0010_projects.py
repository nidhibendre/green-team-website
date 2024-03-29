# Generated by Django 4.2.3 on 2023-08-31 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_team_app", "0009_rename_url_socialmedialink_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="Projects",
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
                ("image", models.ImageField(upload_to="projects/")),
                ("description", models.TextField()),
            ],
        ),
    ]
