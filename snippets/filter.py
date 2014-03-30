from snippets.models import Snippet
import django_filters

class SnippetFilter(django_filters.FilterSet):
	code = django_filters.CharFilter(name='code', lookup_type='contains')
	class Meta:
		model = Snippet
		fields = ('code',)