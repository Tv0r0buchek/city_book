from core.views import main
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main),
    path("moscow/", main, name = "Москва"),
    path("spb/", main, name="Санкт-Петербург"),
    path("ast/", main, name="Астрахань"),
    path("london/", main, name="Лондон"),
]
