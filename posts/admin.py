from django.contrib import admin

from .models import Post,PostFile

class PostFileInlineAdmin(admin.StackedInline):
    model = PostFile
    fields = ('file',)
    extra = 0 #dont have default template file
    
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('user','caption','title','is_active','created_time')
    list_display = ('title','user','is_active','created_time')
    readonly_fields= ('created_time',)
    inlines = (PostFileInlineAdmin,)
