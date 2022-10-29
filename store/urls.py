from django.urls import path
from .views import ProductListView, ProductDetail

app_name = 'store'
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:id>/<slug:slug>/', ProductDetail.as_view(), name='product_detail')
]
