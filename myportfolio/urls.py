from django.contrib import admin
from django.urls import path
from . import views  # Import the views file

urlpatterns = [
    path('', views.home, name='home'),  # Map the home view to the root URL
    path('admin/', admin.site.urls),
]
