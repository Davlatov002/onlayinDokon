from django.urls import path
from . import views


urlpatterns = [

    # Praduct urls
    path('praducts-search/',views.product_search, name='praducts-search'),
    path('praducts-create/',views.praduct_created, name='praducts-create'),
    path('praducts-get/',views.praduct, name='praducts-get' ),
    path('praduct-expensive/',views.praduct_expensive, name='praduct-expensive' ),
    path('praduct-get-id/<str:pk>/',views.praduct_id, name='praduct-get-id'),
    path('praduct-update/<str:pk>/',views.praduct_update, name='praduct-update' ),
    path('praduct-delete/<str:pk>/',views.praduct_delete, name='praduct-delete' ),

    #  Category  urls
    path('categorys-create/',views.category_creat, name='categorys-create' ),
    path('category-delete/<str:pk>/',views.category_delet, name='category-delete'),
    path('category-update/<str:pk>/',views.category_update, name='category-update' ),
    path('categorys-get/',views.categorys, name='categorys-get' ),
    path('categorys-get_id/<str:pk>/',views.categorys_get_id, name='categorys-get_id' ),

]

