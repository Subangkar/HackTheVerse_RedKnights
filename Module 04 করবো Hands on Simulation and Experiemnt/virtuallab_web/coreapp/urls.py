from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from coreapp import views

app_name = 'coreapp'

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('lab/', views.lab, name='lab'),
    path('experiment/<int:id>', views.experiment, name='experiment'),
    path('class/', views.classview, name='class'),
    path('result/', views.result, name='result'),
    path('recording/', views.recording, name='recording'),
    path('assignment/', views.lab, name='assignment'),
]
