from django.contrib import admin

# added manually
from .models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content')
    list_filter = ('created_at', )
    serach_fields = ('user', 'content')


admin.site.register(Comment, CommentAdmin)