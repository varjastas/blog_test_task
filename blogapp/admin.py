from django.contrib import admin
from .models import Blog, Tag
from sorl.thumbnail.admin import AdminImageMixin 


class BlogAdmin(AdminImageMixin, admin.ModelAdmin): 
    list_display = ('title', 'created_at', 'display_tags')
    search_fields = ('title', 'content')
    list_filter = ('tags', 'created_at')
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('tags',)

    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    display_tags.short_description = 'Tags'
    
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
admin.site.register(Tag, TagAdmin)
admin.site.register(Blog, BlogAdmin)