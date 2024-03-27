from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup_api'),
    path('login', views.login, name='login_api'),
    path('create_medicine', views.create_medicine, name='createmedicineapi'),
    path('list_medicine', views.list_medicine, name='retrievemedicineapi'),
    path('<int:pk>/update_medicine', views.update_medicine, name='updatemedicineapi'),
    path('<int:pk>/delete_medicine', views.delete_medicine, name='deletemedicineapi'),
    path('search_medicine/', views.search_medicine, name='searchmedicineapi'),

]