#created manually

# comments/urls.py
from django.urls import path
from .views import comment_create_view

urlpatterns = [
    # path('post/<int:post_id>/comment/', comment_create_view, name='comment_create'),
    path('', comment_create_view, name='comment_create'),
]