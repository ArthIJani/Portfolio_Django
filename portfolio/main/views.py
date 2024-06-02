from django.shortcuts import render, get_object_or_404
from .models import Project, Tag, BlogPost, Category


def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, "home.html", {"projects": projects, "tags": tags})


def contact(request):
    return render(request, "contact.html")

def resume(request):
    return render(request, "resume.html")

def blogs(request):
    blogs = BlogPost.objects.all()
    category = Category.objects.all()
    return render(request, "blogs.html", {"blogs": blogs, "category": category})

def blog_detail(request, id):
    blog_detail = get_object_or_404(BlogPost, pk=id)
    return render(request, 'blog_detail.html', {"blog":blog_detail})


def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {"project": project})
