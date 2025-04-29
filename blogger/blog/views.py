# blog/views.py

from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost
from django.shortcuts import render, get_object_or_404


def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'detail.html', {'post': post})

def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirect to your homepage or post list
    else:
        form = BlogPostForm()
    
    return render(request, 'create.html', {'form': form})
