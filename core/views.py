from django.shortcuts import render
from django.db.models import Count
from core.models import Video, Comment


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

    video_tags_id = video.tags.values_list("id", flat=True)
    similar_videos = Video.objects.filter(tags__in=video_tags_id).exclude(id=video.id)
    similar_videos = similar_videos.annotate(same_tags=Count("tags")).order_by("-same_tags", "-date")[:25]

    comment = Comment.objects.filter(active=True, video=video).order_by('-date')


    context = {
        "videos": video,
        "comment":comment,
        "similar_videos": similar_videos
    }
    return render(request, "video.html", context)


def ajax_save_comment(request):
    if request.method == "POST":
        pk = request.POST.get("id")
        video = Video.objects.get(id=pk)
        user = request.user
        comment = request.POST.get("comment")

        new_comment = Comment.objects.create(comment=comment, user=user, video=video)
        new_comment.save()

        response = "Comment"
        return HttpResponse(response)


    else:
        pass
