from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('curriculum/', views.curriculum_view, name='curriculum'),
    path('news/', views.news_view, name='news'),
    path('news/<str:slug>/', views.news_detail_view, name='news_detail'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('admission/', views.admission_view, name='admission'),
    path('contact/', views.contact_view, name='contact'),
]
