from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('records/', views.records_table , name='records'),
    path('record/<int:pk>/', views.customer_record, name='customer-record'),
    path('record/<int:pk>/delete/', views.delete_record, name='delete-record'),
    path('add_record/', views.add_record, name='add-record'),
    path('record/<int:pk>/update/', views.update_record, name='update-record'),
]