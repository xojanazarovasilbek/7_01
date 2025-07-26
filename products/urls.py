from  django.urls import path
from .views import ichimlik_list, ichimlik_datail,delete_ichimlik, ichimlik_create

urlpatterns = [
    path('', ichimlik_list, name='ich_list'),
    path('detail/<int:pk>',ichimlik_datail, name='detail' ),
    path('delete/<int:pk>',delete_ichimlik, name='delete' ),
    path('delete/',ichimlik_create, name='create' ),

]