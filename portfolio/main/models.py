from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
    

class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
        )
    image = models.ImageField(upload_to="project_images/")

    def __str__(self):
        return f"{self.project.title} Image"


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, related_name="category")
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    blog = models.ForeignKey(
        BlogPost, related_name="blog_images", on_delete=models.CASCADE
        )
    blog_image = models.ImageField(upload_to="blog_images/")

    def __str__(self):
        return f"{self.blog.title} Image"