import django_filters
from django_filters import DateFilter
from bookcat.models import Book

class BookFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr="gte")
    end_date = DateFilter(field_name="date", lookup_expr="lte")
    class Meta:
        model = Book
        fields = {'title_description': ['contains'],
                  'contributors': ['contains'],
                  # 'category',
                  'language': ['exact']
                }