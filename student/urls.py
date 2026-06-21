from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('all/', views.student_all_record, name='student_all'),
    path('form/', views.student_form, name='student_form'),
    path('delete/<int:s_id>/', views.student_delete, name='student_delete'),
    path('update/<int:s_id>/', views.student_update, name='student_update'),
]