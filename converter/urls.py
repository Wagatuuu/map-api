from django.urls import path
from converter import views

urlpatterns = [
    path('info', views.NoiseInfoView.as_view()),
    path('register', views.register, name=('register')),
    path('login', views.TokenView.as_view()),
    path('upload', views.upload, name=('upload')),
]
