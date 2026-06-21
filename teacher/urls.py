from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('all/', views.teacher_all_record, name='teacher_all'),
    path('form/', views.teacher_form, name='teacher_form'),
    path('delete/<int:t_id>/', views.teacher_delete, name='teacher_delete'),
    path('update/<int:t_id>/', views.teacher_update, name='teacher_update'),
]