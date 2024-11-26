from django.urls import path
from apps.buku import views


urlpatterns = [
    path('',views.index)
]

