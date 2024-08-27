from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('team/', views.team , name='team'),
    path('create_messaging/', views.create_messaging, name='create_messaging'),
    path('create_consulting/', views.create_consulting, name='create_consulting'),
    path('create_newsletter/', views.create_newsletter, name='create_newsletter'),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
]
