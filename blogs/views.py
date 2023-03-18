from django.shortcuts import render, redirect

# Create your views here.

from .models import BlogPost
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

from django.http import Http404

def index(request):
    """The home page for blogs."""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit a post."""
    post = BlogPost.objects.get(id=post_id)
    title = post.title
    text = post.text
    
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = BlogForm(instance=post)
    else:
        # POST data submitted; process data.
        form = BlogForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

