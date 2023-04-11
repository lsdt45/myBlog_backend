from django_filters import FilterSet, CharFilter
from ..models import Article


class ArticleFilter(FilterSet):
    category = CharFilter(field_name='category', lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['category']
