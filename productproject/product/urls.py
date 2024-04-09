from django.urls import path
from .views import Add_product, List_product, Detail_product, Update_product, Delete_product

urlpatterns = [
    path('add/', Add_product.as_view()),
    path('list/', List_product.as_view()),
    path('detail/<int:pk>/', Detail_product.as_view()),
    path('update/<int:pk>/', Update_product.as_view()),
    path('delete/<int:pk>/', Delete_product.as_view()),
]
