from django.views.generic import ListView, DetailView
from .models import Category, Producer, Product
from .filters import ProductFilter


class ProductListView(ListView):
    model = Product
    template_name = 'store/products/product_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return ProductFilter(self.request.GET, queryset=queryset).qs

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list
        queryset.filter(is_active=False)
        my_filter= ProductFilter(self.request.GET, queryset=queryset)
        print(queryset)
        return super().get_context_data(
            object_list=queryset,
            filter=my_filter,
            **kwargs)