from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('merge/', views.merge, name = 'merge'),
    path('split/', views.split, name = 'split'),
    path('compressPdf/', views.compress, name = 'compress'),
    path('compress/download/', views.download)

]