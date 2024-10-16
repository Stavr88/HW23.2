from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, is_published

app_name = BlogConfig.name


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('<int:pk>/view', BlogDetailView.as_view(), name='blog_detail'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
    path('<int:pk>/', is_published, name='is_published'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
