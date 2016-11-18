from django.shortcuts import render, get_object_or_404
from Blog.models import Post, Category

# Create your views here.
def blogIndex(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'Blog/index.html', {'posts':posts})

def postView(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'Blog/post.html', {'post':post})

def categoryView(request):
    categories = Category.objects.all()
    return render(request, 'Blog/category.html', {'categories':categories})

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'Blog/view_category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5]
    })
