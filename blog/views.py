from django.shortcuts import render , get_object_or_404, redirect
from django.http import Http404
from .models import Post
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Blog
def post_list(request):
    posts = Post.objects.all() 
    # search
    query = request.GET.get("q")
    if query:
        posts=Post.objects.filter(Q(title__icontains=query) ).distinct()
            
    
    paginator = Paginator(posts, 2) # 10 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    
   
        
    return render(request,'blog/post_list.html',{'posts':posts, page:'pages'})

def post_detail(request, id,title):
    try:
        post = Post.objects.get(id=id)
        context = {'post': post}
    except Post.DoesNotExist:
        return render(request,'base/notfound.html')
    return render(request,'blog/post_detail.html',context)
