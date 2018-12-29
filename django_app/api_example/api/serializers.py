from rest_framework import serializers
from api_example.models import ApiExample

class Api_exampleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ApiExample
        fields = ('title','body','created')