from django.urls import path
from .views import project_list, home, contact, project_detail, contact_success
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),  # Página de inicio
    path('projects/', project_list, name='project_list'),
    path('project/<int:id>/', project_detail, name='project_detail'),
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)