from django.urls import path, include
from posts import views


app_name = "posts"

urlpatterns = [
    path('order/', views.order_food, name="order_food"),
]