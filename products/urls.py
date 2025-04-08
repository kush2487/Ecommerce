from django.urls import path
from products import views 

urlpatterns = [
    path('changing_api/', views.changing_api),
    path('get_products/', views.get_products),
    path('get_products_id/<int:id>', views.get_products_id),
    path('creating_product', views.creating_product),
    path('update_product/<int:id>', views.update_product),
    path('update_product_full/<int:id>', views.update_product_full),
    path('delete_product/<int:id>', views.delete_product),
]
