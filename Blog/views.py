from django.shortcuts import render
from .models import *

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    renderDic = {
        'jumbotron': "The Blog",
        'pageTitle': "The Blog - Roymond.net",
        'posts' : posts,
        'active': 'blog'
    }
    return render(request, 'blog/post_list.html', renderDic)

def category_list(request, catName):
    posts = Post.objects.filter(categories__slug__iexact=catName).order_by("post_title")
    category = Category.objects.filter(slug__iexact=catName).get()
    renderDic = {
        'jumbotron': category.name,
        'pageTitle': "Posts with the '" + category.name + "' tag - Roymond.NET",
        'posts' : posts,
        'active': 'blog'
    }
    return render(request, 'blog/category_list.html', renderDic)

def post_detail(request, postSlug):
    post = Post.objects.filter(slug__iexact=postSlug).get()
    print(post.content)
    renderDic = {
        'jumbotron' : post.post_title,
        'pageTitle' : post.post_title,
        'post' : post,
        'active': 'blog'
    }
    return render(request, 'blog/post_detail.html', renderDic)
