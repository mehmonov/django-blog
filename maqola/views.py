from django.shortcuts import render
from .models import Maqola, Comment, Like

def index(request):
    maqolalar = Maqola.objects.all().order_by("created_at")
    
    return render(request, "index.html", {"maqolalar": maqolalar})

def detail(request, id):
    
    
    maqola = Maqola.objects.get(id=id)
    maqola.views = maqola.views + 1
    
    maqola.save()
    comments = Comment.objects.filter(maqola=maqola, status=True)

    likes = Like.objects.filter(maqola=maqola).count()
    

    return render(request, "detail.html", {"maqola": maqola, "comments": comments, "likes_count": likes})
