# from django.shortcuts import render

# Create your views here.
# comments/views.py
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Comment, Post
from django.urls import reverse

@login_required
def comment_create_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            # return redirect('post_detail', post_id=post_id)
            # return redirect(reverse('post-detail', args=[post_id]))
            return redirect(f'/blog/post/{post_id}/')
    else:
        form = CommentForm()
    return render(request, 'comments/comment_form.html', {'form': form})