from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('order',views.order,name='order'),
    path('register',views.sign_in,name='signing'),
    path('add_code',views.new_code,name='pro_code'),
    path('<int:ss>/verify',views.verify,name='verify'),
    path('about',views.about,name='about'),
    path('community',views.community,name='community'),
#    path('<int:page>/results',views.search,name='results'),
]