from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Default admin site URL
    path('home/', views.home, name='home'),
    path('capture_pressure/', views.capture_pressure, name='pressures'),
    path('import_view/', views.import_view, name='imports'),
]