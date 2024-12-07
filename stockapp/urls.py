from django.urls import path
from . import views

urlpatterns = [
    path("prediction.html", views.prediction, name="prediction")
]