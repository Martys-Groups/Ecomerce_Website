from . import views
from django.urls import path,include

urlpatterns = [
    path("", views.index,name="shop"),
    path("products/<int:id>", views.product_view,name="product_view"),
]
