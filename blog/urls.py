#created manually
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('login/', views.login_view, name='login'),     #login url
    path('logout/', views.logout_view, name='logout'),  #logout url
    path('register/', views.register, name='register'),     #register url
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/', include('comments.urls')),       #comments
    path('post/new/', views.post_new, name='post_new'),
    path('post/<pk>/edit/', views.post_edit, name='post_edit'),
    path('search/', views.search, name='search'),   #search url
    
]
