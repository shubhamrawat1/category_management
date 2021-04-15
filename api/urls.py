from django.urls import path
from . import views


urlpatterns = [
    path('category-create/', views.CategoryCreateAPIView.as_view(), name='category-create'),
    path('category-update/<pk>/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category-view/<pk>/', views.CategoryViewAPIView.as_view(), name='category-view'),
    path('category-delete/<pk>/', views.CategoryDeleteAPIView.as_view(), name='category-delete'),
    path('categories-list/', views.CategoryListAPIView.as_view(), name='categories-list'),
    ]






