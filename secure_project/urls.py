from django.contrib import admin
from django.urls import path, include
from chat import views  # Import your app's views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),  # Ensure this route exists
]
