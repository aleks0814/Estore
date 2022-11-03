from django.urls import path
from .views import ProductListView, ProductDetail, product_detail

app_name = 'store'
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:id>/<slug:slug>/', product_detail,
         name='product_detail'),
]
