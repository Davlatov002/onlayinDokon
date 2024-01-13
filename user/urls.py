from django.urls import path
from . import views


urlpatterns = [

    #  Basket urls
    path('basket-add/',views.basket_add, name='basket-add'),
    path('basket-delete/<str:pk>/',views.basket_delet, name='basket-delete'),
    path('baskets-get/',views.baskets_get, name='baskets-get' ),
    path('baskets-get-id/<str:pk>/',views.baskets_get_id, name='baskets-get-id'),

    #  Costomer urls
    path('costomer-create/',views.costomer_creat, name='costomer-create' ),
    path('costomer-delete/<str:pk>/',views.costomer_delet, name='costomer-delete'),
    path('costomer-update/<str:pk>/',views.costomer_update, name='costomer-update'),
    path('costomer-get/',views.costomer_get, name='costomer-get' ),
    path('costomer-get-id/',views.costomer_get_id, name='costomer-get-id' ),

]