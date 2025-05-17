
import django
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from .views import testView

urlpatterns = [
    path('test/', testView.as_view()),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


