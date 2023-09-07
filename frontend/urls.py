from django.urls import path
from . import views


app_name = 'frontend'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('<int:section_id>/', views.redirect_to_section, name='redirect_to_section'),
   

]


# Geçersiz URL'ler için genel yakalama URL'si
urlpatterns += [
    path('<str:invalid_url>/', views.invalid_url_redirect, name='invalid_url_redirect'),
]