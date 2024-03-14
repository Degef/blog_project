from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView


urlpatterns = [
    # path('', views.home, name='home'),
    path('about/', views.about, name='about'),
	path('', PostListView.as_view(), name='home'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
]