from django.contrib import admin
from.models import *
from user import views
from django.template.response import TemplateResponse
from django.urls import path

class MyAdmin(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('orders/', self.admin_view(self.my_view)),
        ]
        return my_urls + urls

    def my_view(self, request):
        # ...
        o=Orders.objects.all()
        os=[]
        for i in o:
            if i.state==False:
                os.append(i)
        context = dict(
           # Include common variables for rendering the admin template.
           self.each_context(request),
           # Anything else you want in the context...,
           i=os
        )
        return TemplateResponse(request, "user/kivy.html", context)

admin_site = MyAdmin(name='myadmin')
# Register your models here.
admin_site.register(Serial)
admin_site.register(UserOn)
admin_site.register(User)
admin_site.register(Orders)
admin_site.register(Product)
admin_site.register(Advertisement)
#admin.site.register(OrderState)
admin_site.register(Setting)
admin_site.register(FromComp)
admin_site.register(CommentsB)
admin_site.register(CommentsP)
#from django.contrib import admin



