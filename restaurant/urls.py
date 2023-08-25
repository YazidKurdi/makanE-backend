from django.urls import path
from . import views

urlpatterns = [
    path('api/menu-list/', views.FoodCategoryList.as_view()),
    path('api/menu-items/<str:slug>/', views.MenuItemDetail.as_view(), name='menu-item-detail'),
    path('api/', views.MenuItemSearch.as_view()),
    # Add more API endpoints if needed
]
