from django.contrib import admin
from django.urls import path,re_path
from . import views


app_name='articles'

urlpatterns = [
    path('', views.article_list,name="list"),
    path(r'create/', views.article_create, name="create"),
    path('<slug>/',views.article_detail,name="detail"),
    #re_path('(?P<slug>[\w-]+)$/',views.article_detail,name="detail"),

]
