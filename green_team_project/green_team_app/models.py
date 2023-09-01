from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from PIL import Image

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    # Resize the cover photo to the desired aspect ratio (398x265)
        if self.image:
            img = Image.open(self.image.path)
            img.thumbnail((398, 265))
            img.save(self.image.path)

class BlogPost(models.Model):
    cover_photo = models.ImageField(upload_to='blog_covers/')
    author = models.ForeignKey('TeamMember', on_delete=models.SET_NULL, null=True, blank=True)
    cover_source = models.CharField(max_length=100, null=True)
    other_author = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=2000)
    subtitle = models.CharField(max_length=2000, blank=True)
    body_text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    # Resize the cover photo to the desired aspect ratio (398x265)
        if self.cover_photo:
            img = Image.open(self.cover_photo.path)
            img.thumbnail((398, 265))
            img.save(self.cover_photo.path)


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team_images/', default='team_images/default_profile_picture.png')

    def __str__(self):
        return self.name


class SocialMediaLink(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name

class Footer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    social_media_links = models.ManyToManyField(SocialMediaLink)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"



    
