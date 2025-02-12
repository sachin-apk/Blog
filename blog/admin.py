from django.contrib import admin
#imported manually
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','updated_at')
    list_filter = ('created_at', )
    serach_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)
