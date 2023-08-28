from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('register/', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('homepage/', views.homepage, name='homepage'),
    path('adminpage/',views.adminpage, name='adminpage'),

    path('create_category/', views.create_category, name='create_category'),
    path('get_categories/', views.get_categories, name='get_categories'),
    path('add_article/', views.add_article, name='add_article'),
    path('get_articles/', views.get_articles, name='get_articles'),
    path('get_articles_by_category/', views.get_articles_by_category, name='get_articles_by_category'),
]