from django.shortcuts import render, redirect   #added manually: redirect
#imported manually
from django.contrib.auth.models import User
#for forms
from .models import Post
from .forms import PostForm
#for user authentication
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout 
#for registration form
from .forms import RegistrationForm
#for comments
from comments.models import Comment 


# Create your views here.

# views for blogs
def post_list(request):
    # posts = Post.objects.all()
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html',{'posts': posts})

# view for detailed blogs
def post_detail(request, pk=None):
    posts = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': posts})


#views for creating and editing blog posts
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


#changed from above view function
# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_new.html', {'form': form})


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


#login views
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
    return render(request, 'blog/login.html', {})
    
#logout views
def logout_view(request):
    logout(request)
    return redirect('post_list')


#search request 
def search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})


#views for user registration
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html', {'form': form})