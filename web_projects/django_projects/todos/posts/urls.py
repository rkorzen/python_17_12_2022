from django.urls import path

from posts.views import post_list, post_details

urlpatterns = [
    path("", post_list),
    path("<int:id>/", post_details),
]