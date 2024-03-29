# Generated by Django 4.2.3 on 2023-08-01 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_team_app", "0005_blogpost_other_author_alter_blogpost_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="cover_source",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="cover_photo",
            field=models.ImageField(upload_to="blog_covers/"),
        ),
    ]
