from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("predict/", views.predict),
    path("predict/result/", views.result),
    path("diet/", views.diet),
    path("predict/result/diet/",views.diet),
    path("recommend/",views.recommend),
    path("home/",views.home),
    path("team/",views.team),
    path("diet/below25/",views.below25),
    path("diet/age25/",views.age25),
    path("diet/above50",views.above50),
    path("predict/result/diet1/",views.diet),
    path("predict/result/diet1/below25",views.below25),
    path("predict/result/diet1/age25",views.age25),
    path("predict/result/diet1/above50",views.above50), 
]
