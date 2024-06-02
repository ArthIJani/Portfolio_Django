from django.contrib import admin
from .models import Tag, Project, ProjectImage, BlogPost, Category, BlogImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    inlines = [ProjectImageInline]
    search_fields = ("title", "description")
    list_filter = ("tags",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1

class BlogPostAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline]
    list_filter = ("category",)



admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogImage)
