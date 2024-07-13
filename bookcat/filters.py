import django_filters
from django_filters import DateFilter, ChoiceFilter
from bookcat.models import Book

class BookFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr="gte")
    end_date = DateFilter(field_name="date", lookup_expr="lte")
    temp = ChoiceFilter(field_name="category", lookup_expr="icontains",
                        choices=(
                            ('Printed Copies of Codices', 'Printed Copies of Codices'),
                            ('Incunabula', 'Incunabula'),
                            ('Opera', 'Opera'),
                            ('Opuscula', 'Opuscula'),
                            ('Bucolica Et Georgica', 'Bucolica Et Georgica'),
                            ('Eclogae', 'Eclogae'),
                            ('Georgica', 'Georgica'),
                            ('Aeneis', 'Aeneis'),
                            ('Centones)', 'Centones'),
                            ('Translations', 'Translations'),
                            ('Travesties', 'Travesties'),
                            ('The Bancroft Collection of English Versions of Virgil', 'The Bancroft Collection of English Versions of Virgil'),
                            ('Works About Virgil And His Poems', 'Works About Virgil And His Poems'),
                            ('', 'Any'),)
                            )
    class Meta:
        model = Book
        fields = {'title_description': ['contains'],
                  'contributors': ['contains'],
                  'language': ['contains']
                }