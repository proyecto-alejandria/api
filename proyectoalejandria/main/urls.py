from django.urls import path

from . import views


urlpatterns = [
    path("bootstrap/", views.BootstrapView.as_view()),
]
