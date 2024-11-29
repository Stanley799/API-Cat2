from django.urls import path

urlpatterns = [
    # Example: path('', views.home, name='home'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),  # This expects 'posts/urls.py' to exist.
]