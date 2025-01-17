
from django.contrib import admin
from django.urls import path
from polls import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("login/", views.createUser)
]
