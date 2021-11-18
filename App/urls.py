from django.urls import path
from App import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/",views.index, name= "index"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("about/", views.about, name="about"),
    path("prediction/", views.prediction_view, name="prediction"),
    path("positive/", views.positive, name="positive"),
    path("negative/", views.negative, name="negative")
]
