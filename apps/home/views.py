from django.shortcuts import render, redirect
from apps.home.models import Post, MediaFiles
# Create your views here.

def index(request):


    if request.method == "POST":
        title = request.POST.get('title')
        post = Post(title=title)
        post.save()
        print(request.FILES.getlist('img'))
        for f in request.FILES.getlist('img'):
            media = MediaFiles(post=post, img=f)
            media.save()
        return redirect('home:index_page')
    return render(request, 'home/index.html', {})
