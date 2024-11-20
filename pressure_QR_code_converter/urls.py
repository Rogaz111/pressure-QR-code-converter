from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from my_app import views
from my_app.views import generate_qr_code

urlpatterns = [
    path('admin/', admin.site.urls),  # Default admin site URL
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('capture_pressure/', views.capture_pressure, name='pressures'),
    path('import_view/', views.import_view, name='imports'),
    path('generate_qr_code/', generate_qr_code, name='generate_qr_code'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)