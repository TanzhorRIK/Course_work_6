from django.contrib import admin
from blog.models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')
    list_filter = ('title', 'is_published')
    prepopulated_fields = {'slug': ('title',)}