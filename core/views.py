from django.shortcuts import render
from django.http import HttpResponse

from core.models import Video


def index(request):
    video = Video.objects.filter(visibility="public")

    context = {
        "videos": video,
    }
    return render(request, "index.html", context) 



def video_detail(request, pk):
    video = Video.objects.get(id=pk)
    
    video.views = video.views + 1
    video.save()

    context = {
        "videos": video,
    }
    return render(request, "video.html", context)