# Generated by Django 4.2.3 on 2023-07-31 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_team_app", "0003_remove_blogpost_author_name_blogpost_author_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="teammember",
            old_name="role",
            new_name="position",
        ),
        migrations.RemoveField(
            model_name="teammember",
            name="bio_url",
        ),
        migrations.AlterField(
            model_name="teammember",
            name="image",
            field=models.ImageField(
                default="team_images/default_profile_picture.png",
                upload_to="team_images/",
            ),
        ),
    ]