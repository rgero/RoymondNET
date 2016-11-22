from django.shortcuts import render, get_object_or_404
from Blog.models import Post, Category, Tag

# Create your views here.
def blogIndex(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'Blog/index.html', {'posts':posts,'active': "blog",'jumbotron': "The Blog"})

def postView(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'Blog/post.html', {'post':post,'active': "blog",'jumbotron': post.title})

def categoryView(request):
    categories = Category.objects.all()
    return render(request, 'Blog/category.html', {'categories':categories,'active': "blog",'jumbotron': "The Blog"})

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'Blog/view_category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5],
        'active': "blog",
        'jumbotron': "The Blog"
    })

def view_tags(request, slug):
    desiredTag = get_object_or_404(Tag, slug=slug)
    return render(request, 'Blog/view_tag.html', {
        'tag': desiredTag,
        'posts': Post.objects.filter(tags__exact=desiredTag),
        'active': "blog",
        'jumbotron': "The Blog"
    })
