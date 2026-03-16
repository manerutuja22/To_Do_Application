from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.task_list),
    path("update/<int:id>/", views.update_task, name="update"),
    path('delete/<int:id>/', views.delete_task, name="delete"),
    path('complete/<int:id>/', views.complete_task, name="complete"),
]