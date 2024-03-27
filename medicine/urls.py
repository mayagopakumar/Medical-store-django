from . import views
from django.urls import path

urlpatterns = [
        path('create/',views.medicine_create,name='addmedicine'),
        path('retrieve/',views.medicine_read,name='readmedicine'),
        path('update/<int:id>/',views.medicine_edit,name='editmedicine'),
        path('delete/<int:pk>',views.medicine_delete,name='deletemedicine'),
        path('listing/',views.listing,name='page_list'),
        path('search/',views.medicine_search,name="search")
    ]