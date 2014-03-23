from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet#, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# class SnippetSerializer(serializers.Serializer):
# 	pk = serializers.Field()
# 	title = serializers.CharField(required=False, max_length=100)
# 	code = serializers.CharField(widget=widgets.Textarea, max_length=100000)
# 	linenos = serializers.BooleanField(required=False)
# 	language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
# 	style = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')
	
# 	def restore_object(self, attrs, instance=None):
# 		if instance:
# 			instance.title = attrs['title']
# 			instance.code = attrs['code']
# 			instance.linenos = attrs['linenos']
# 			instance.language = attrs['language']
# 			instance.style = attrs['style']
# 			return instance
# 		return Snippet(**attrs)
#------------------------------------------------------------------------------------
# class SnippetSerializer(serializers.ModelSerializer):
# 	owner = serializers.Field(source='owner.username')

# 	class Meta:
# 		model = Snippet
# 		field = ('id', 'owner', 'title', 'code', 'linenos', 'language', 'style')
		
# class UserSerializer(serializers.ModelSerializer):
# 	snippets = serializers.PrimaryKeyRelatedField(many=True)

# 	class Meta:
# 		model = User
# 		field = ('id', 'username', 'snippets')

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.Field(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

	class Meta:
		model = Snippet
		fields = ('url', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')
		
class UserSerializer(serializers.HyperlinkedModelSerializer):
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail')

	class Meta:
		model = User
		fields = ('url', 'username', 'snippets')
