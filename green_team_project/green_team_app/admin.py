from django.contrib import admin
from .models import BlogPost, TeamMember, SocialMediaLink, Project
from .forms import BlogPostForm

admin.site.register(Project)

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostForm

admin.site.register(BlogPost, BlogPostAdmin)

admin.site.register(TeamMember)

class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')

admin.site.register(SocialMediaLink, SocialMediaLinkAdmin)


