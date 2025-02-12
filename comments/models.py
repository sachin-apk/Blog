from django.db import models

# Create your models here.
# comments/models.py
# from django.db import models
from django.contrib.auth.models import User
from blog.models import Post  # assuming your blog app has a Post model

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} commented on {self.post.title}"
