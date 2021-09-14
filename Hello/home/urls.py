from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name= "homepage"),
    path('contactUs', views.contactUs, name = "contactUs"),
    path("signUp", views.signUp, name = "signUp"),
    path("login", views.login, name = "login"),  
    path("logout", views.logout, name = "logout"),
    path("add/todo", views.add_toDo, name = "add_toDo"),
    path('delete_toDo/<int:id>', views.delete_toDo, name = "delete_toDo"),
    path('update_status_toDo/<int:id>/<str:status>', views.update_status_toDo, name = "update_status_toDo")
    
]
