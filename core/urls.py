from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('messages/', views.MessageCreateView.as_view(), name='add-message'),
    path('about/', views.about_page, name='about'),
    path('portfolio/', views.portfolio_page, name='portfolio'),
    path('portfolio/<str:category>', views.portfolio_page, name='portfolio'),
    path('contact/', views.contact_page, name='contact')
]
