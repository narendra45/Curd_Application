from django.urls import path
from django.views.generic import TemplateView

from product import views

urlpatterns = [
#     path('add_tag/',views.addTags,name='add_tag'),
    # path('view_tag/',views.viewAllTags,name='view_tag'),
    path('add_product/',views.addProduct,name='add_product'),
    path('view_all/',views.viewAllProducts,name='view_all'),
    path('edit_product/<product_id>', views.editProduct, name='edit_product'),
    path('delete_product/<product_id>', views.deleteProduct, name='delete_product'),
]