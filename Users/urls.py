from django.urls import path
from .import views

urlpatterns = [
    path('register',views.register,name='register'),
    # path('<str:ref_code>/', views.main, name='refferal'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]
