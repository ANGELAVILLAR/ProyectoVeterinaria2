from django.urls import path

from core import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('portfolio/', views.portfolio, name="portfolio"),
    #path('petshop/', views.petshop, name="tienda"),
    path('contact/', views.contact, name="contact"),    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)