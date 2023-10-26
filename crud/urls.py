from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('update/<int:todo_id>', views.update, name='update'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
    path('edit/<int:todo_id>/', views.edit_todo, name='edit'),

]