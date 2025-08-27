
from django.urls import path
from product import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view()),
    path('category/<int:pk>/', views.CategoryDetailView.as_view()),
    path('review/', views.ReviewListView.as_view()),
    path('review/<int:pk>/', views.ReviewDetailView.as_view()),
    path('product/', views.ProductListView.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view())

    ]