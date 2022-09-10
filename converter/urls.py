from django.urls import path
from converter import views

urlpatterns = [
    path('info', views.NoiseInfoView.as_view()),
]
