from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('team/', views.team , name='team'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/', views.blog_list, name='blog'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('create_messaging/', views.create_messaging, name='create_messaging'),
    path('create_consulting/', views.create_consulting, name='create_consulting'),
    path('create_newsletter/', views.create_newsletter, name='create_newsletter'),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
]
