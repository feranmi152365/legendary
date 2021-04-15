from django.urls import path
from .import views

urlpatterns = [
    # path('', views.main, name='refferal'),
    path('<str:ref_code>/', views.main, name='refferal')
]
