import  django_filters
from django.forms import CheckboxSelectMultiple
from django_filters import widgets
from .models import Category, Producer, Product

class ProductFilter(django_filters.FilterSet):
    CHOICES = (
        ('name', 'Alphabetical ascending'),
        ('-name', 'Alphabetical descending'),
        ('price', 'Price ascending'),
        ('-price', 'Price descending')
    )
    name = django_filters.CharFilter(label='Name',lookup_expr='icontains')
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), widget=CheckboxSelectMultiple)
    price = django_filters.RangeFilter(field_name='price')
    order_by_name = django_filters.ChoiceFilter(label='Sort by', choices=CHOICES, method='filter_by_ordering')
    in_stock = django_filters.BooleanFilter(field_name='in_stock')


    def filter_by_ordering(self, queryset,name, value):
        return queryset.order_by(value)

    def filter_is_active(self, queryset,name, value):
        print(name)
        # construct the full lookup expression.
        lookup = '__'.join([name, 'isnull'])
        return queryset.filter(**{lookup: False})