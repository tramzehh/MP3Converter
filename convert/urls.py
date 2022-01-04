from django.urls import path
from convert import views

urlpatterns = [
    path('', views.ConverterPage.as_view(), name='home'),
    path('convert/', views.convert_video_to_mp3, name='convert'),
]