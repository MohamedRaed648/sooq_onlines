from django.urls import path
from . import views
app_name='sooq'

urlpatterns=[
    path('show_detail_product/<int:id>',views.Product_detail),
    path('Update_Product/<int:id>',views.Product_update),
    path('Delete_Product/<int:id>',views.Product_Delete),
    path('Create_Product',views.Product_Create),

]