from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    context = {}
    context['posts']=Posts.objects.all().order_by('-id')[:3]

    return render(request, 'index.html',context)

def about(request):

    return render(request, 'about.html')

def blog(request):
    context = {}
    context['blog']=Posts.objects.all().order_by('-id')
    context['posts']=Posts.objects.all().order_by('-id')

    return render(request, 'blog.html',context)

def contact(request):
    return render(request, 'contact.html')

def post_details(request,pk):
    context = {}
    context["posts"] = Posts.objects.get(id=pk)

    return render(request, 'post-details.html',context )

def comment(request,id):
    comment_user_name = request.POST.get('name')
    comment_user_surname = request.POST.get('surname')
    comment = request.POST.get('message')
    post_id = request.POST.get('post_id')
    comment_obj = Comments.objects.create(
        user_name=comment_user_name,  
        surname=comment_user_surname,
        post = Posts.objects.get(id = post_id ),
        body=comment,
    )
    return redirect('post:index')

def category(request,pk):
    context = {}
    context['posts'] = Posts.objects.filter(category_id=pk)
    return render(request,('index.html'),context,)

def filter_tag(request,pk):
    context = {}
    tag = Tag.objects.get(id=pk)
    context['posts'] = tag.tagged_posts.all()
    return render(request, 'index.html', context,)

def search(request):
    context = {}
    context['posts'] = Posts.objects.filter(title__icontains = request.POST.get('q'))
    return render(request, 'index.html', context)