# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Service, ContactRequest

# def index(request):
#     services = Service.objects.all()
#     return render(request, 'website/index.html', {'services': services})

# def about(request):
#     return render(request, 'website/about.html')

# def services(request):
#     services = Service.objects.all()
#     return render(request, 'website/services.html', {'services': services})

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         message = request.POST['message']
#         ContactRequest.objects.create(
#             name=name,
#             email=email,
#             message=message
#         )
#         return HttpResponse('Спасибо за ваше сообщение!')
#     return render(request, 'website/contact.html')
# #1
# from django.db import models

# class Service(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='services/')

#     def __str__(self):
#         return self.title

# class ContactRequest(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} - {self.email}"
    
#     from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='home'),
#     path('about/', views.about, name='about'),
#     path('services/', views.services, name='services'),
#     path('contact/', views.contact, name='contact'),
# ]


                 #sozdait sait rabota 1

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age  = models.IntegerField()
    email = models.EmailField(unique=True)


    def str(self):
        return f"{self.name} ({self.age} лет)"
    
    from django.http import HttpResponse
from .models import User

def home(request):
    return HttpResponse("tmkvnvkndkvndkvnk")


def user_list(request):
    users = User.objects.all()
    text = ""
    for u in users:
      
      text += f"{u.name}, {u.age}лет, {u.email}<br>"
    return HttpResponse(text)

from django.contrib import admin
from django.urls import path
from db_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('users/', views.user_list)
]

from django.contrib import admin
from models impord, User

admin.site.register(User)

class UserAdmin(admin.ModelAdmin):
list_display = ('name', 'age', 'email', )
search_fields = ('name', 'email',)
list_filter = ('age',)

admin.site.register(User, UserAdmin)