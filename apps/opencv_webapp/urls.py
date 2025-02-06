from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name ='opencv_webapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('uimage/', views.uimage, name='uimage'),
]

urlpatterns += static(settings.MEDIA_URL, 
                      document_root=settings.MEDIA_ROOT)