from django.urls import path
from studentapp import views

urlpatterns = [
    path('index/', views.index,name='index'),
    path('create/',views.create_student,name='create'),
    path('edit/<int:id>/',views.edit_student,name='edit'),
    path('delete/<int:id>/',views.delete_student,name='delete'),
]