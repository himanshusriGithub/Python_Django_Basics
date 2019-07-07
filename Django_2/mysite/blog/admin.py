from django.contrib import admin
from .models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):

    list_display = ('title','slug','publish','author','status',)
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields =('title','body')
    prepopulated_fields = {'slug':('title',)}
    ordering = ('status', 'publish')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
