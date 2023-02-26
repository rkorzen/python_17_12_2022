from django.urls import path

from accounts.views import user_profile_view

urlpatterns = [
    path("", user_profile_view),
]
