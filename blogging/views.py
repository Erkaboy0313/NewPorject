from django.shortcuts import render,redirect
from .forms import CommentForm

from .models import Blog,Comment

def home(request):
    
    blogs = Blog.objects.filter(status = Blog.StatusEnum.PUBLISHED).order_by('-update_time')
    
    context = {
        'blogs':blogs
    }
    
    return render(request,'home.html',context)

def blog_details(request,id):
    blog = Blog.objects.get(id = id)
    
    commetns = Comment.objects.filter(blog = blog,reply__isnull = True)
    
    form = CommentForm()
    
    context = {
        'blog':blog,
        'form':form,
        'comments':commetns
    }
    
    return render(request,'blog_detail.html',context)

def create_comment(request,blog_id):
    if request.method == "POST":
        
        blog = Blog.objects.get(id = blog_id)
        
        form = CommentForm(request.POST)
        if form.is_valid():
            
            form.instance.blog = blog
            form.instance.user = request.user.profile
            
            form.save()
    
    return redirect(request.META.get("HTTP_REFERER"))


    
    

