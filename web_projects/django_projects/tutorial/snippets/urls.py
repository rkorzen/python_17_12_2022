from django.urls import path
from rest_framework import renderers

from snippets import views
from snippets.views import SnippetViewSet

user_list = views.UserViewSet.as_view({"get": "list"})

user_detail = views.UserViewSet.as_view({"get": "retrieve"})

snippet_list = SnippetViewSet.as_view({"get": "list", "post": "create"})

snippet_detail = SnippetViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)

snippet_highlight = SnippetViewSet.as_view(
    {"get": "highlight"}, renderer_classes=[renderers.StaticHTMLRenderer]
)

urlpatterns = [
    path("", views.api_root),
    path("snippets/", snippet_list, name="snippet-list"),
    path("snippets/<int:pk>", snippet_detail, name="snippet-detail"),
    path("snippets/<int:pk>/highlighted/", snippet_highlight, name="snippet-highlight"),
    path("users/", user_list, name="user-list"),
    path("users/<int:pk>", user_detail, name="user-detail"),
]
