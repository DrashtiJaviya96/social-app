from django.urls import path
from .views import PostListCreateView, PostDetailView, HealthView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('health/', HealthView.as_view(), name='health'),
]
