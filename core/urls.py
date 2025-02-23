from django.urls import path
from core import views


urlpatterns = [
    path("", views.index),
    path("watch/<int:pk>/", views.video_detail, name="video_detail"),

    path("ajax-save-comment/", views.ajax_save_comment, name="ajax_save_comment"),
]
