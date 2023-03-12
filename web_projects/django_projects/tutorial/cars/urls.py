from django.urls import path
from cars import views


car_list = views.CarViewSet.as_view({"get": "list", "post": "create"})

car_details = views.CarViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("cars/", car_list, name="car-list"),
    path("cars/<int:pk>", car_details, name="car-detail"),
]
