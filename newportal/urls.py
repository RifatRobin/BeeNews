from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('abc', views.abc, name='abc'),
    path('cnn', views.cnn, name='cnn'),
    path('espn', views.espn, name='espn'),
    path('espnc', views.espnCrick, name='espnCrick'),
    path('gnews', views.gnews, name='gnews'),
]
