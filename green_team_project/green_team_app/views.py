from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, TeamMember, SocialMediaLink, Project
from .forms import BlogPostForm
from django.http import HttpResponseRedirect
from urllib.parse import urljoin
from django.core.mail import EmailMessage
from django.contrib import messages


def home (request):
    social_media_links = SocialMediaLink.objects.all()
    return render(request, 'home.html', {'social_media_links': social_media_links})

def projects(request):
    projects = Project.objects.all()
    social_media_links = SocialMediaLink.objects.all()
    return render(request, 'projects.html', {'projects': projects, 'social_media_links': social_media_links})

def blog_page(request):
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    team_member_pks = TeamMember.objects.values_list('pk', flat=True)
    social_media_links = SocialMediaLink.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts, 'team_member_pks': team_member_pks, 'social_media_links': social_media_links})

def blog_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    social_media_links = SocialMediaLink.objects.all()
    return render(request, 'blog_detail.html', {'blog_post': blog_post, 'social_media_links': social_media_links})

def team(request):
    team_members = TeamMember.objects.all()
    social_media_links = SocialMediaLink.objects.all()
    return render(request, 'team.html', {'team_members': team_members, 'social_media_links': social_media_links})

def team_member_detail(request, pk):
    team_member = get_object_or_404(TeamMember, pk=pk)
    social_media_links = SocialMediaLink.objects.all()
    return render(request, 'team_member_detail.html', {'team_member': team_member, 'social_media_links': social_media_links})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        email_message = EmailMessage(
            subject=subject,
            body=message,
            from_email=email,  # Set the 'from_email' to the user's email
            to=['greenteamaite@gmail.com'],  # Recipient's email(s)
            reply_to=[email],  # Set the "Reply-To" address to the user's email
        )

        email_message.send()

        messages.success(request, 'Email sent successfully!')
        referer = request.META.get('HTTP_REFERER')
        
        # Redirect back to the referer page
        if referer:
            return HttpResponseRedirect(referer)
        else:
            return redirect('home')  # Fallback redirection

    social_media_links = SocialMediaLink.objects.all()
    return render(request, 'base.html', {'footer': footer, 'social_media_links': social_media_links})



