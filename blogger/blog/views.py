# blog/views.py

from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'detail.html', {'post': post})

def home(request):
    post_list = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(post_list, 5)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj})
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirect to your homepage or post list
    else:
        form = BlogPostForm()
    
    return render(request, 'create.html', {'form': form})
