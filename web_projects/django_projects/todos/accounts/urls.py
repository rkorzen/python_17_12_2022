from django.urls import path

from accounts.views import user_profile_view, user_registration

urlpatterns = [
    path("", user_profile_view),
    path("registration", user_registration, name="register"),
]
