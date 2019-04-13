from django.urls import path
from .views import (
    MemListView,
    MemDetailView,
    MemCreateView,
    MemUpdateView,
    MemDeleteView
)

from . import views

urlpatterns = [
    path('', MemListView.as_view(), name='post-home'),
    path('mem/<int:pk>/', MemDetailView.as_view(), name='mem-detail'),
    path('mem/new/', MemCreateView.as_view(), name='mem-create'),
    path('mem/<int:pk>/update/', MemUpdateView.as_view(), name='mem-update'),
    path('mem/<int:pk>/delete/', MemDeleteView.as_view(), name='mem-delete'),
    path('about/', views.about, name='post-about'),
    path('contact/', views.contact, name='post-contact'),
]
