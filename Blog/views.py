from django.shortcuts import render, get_object_or_404
from Blog.models import Post, Category

# Create your views here.
def blogIndex(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'Blog/index.html', {'posts':posts})

def postView(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'Blog/post.html', {'post':post})

def categories(request, slug):
    categories = Categories.objects.all()
    return render(request, 'Blog/category.html', {'categories'})
