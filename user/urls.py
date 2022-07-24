from django.urls import path
from .import views
urlpatterns = [
    path('',views.logi_in,name='log_in'),
    path('home',views.home,name='user_home'),
    path('order',views.order,name='order'),
    path('about',views.about,name='about'),
    path('community',views.community,name='community'),
    path('account',views.setting,name='setting')
]