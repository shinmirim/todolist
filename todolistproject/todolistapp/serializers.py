from rest_framework import serializers
from .models import todo
from .models import tag

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ('number', 'title', 'detail', 'tag', 'createDate', 'updateDate','planDate','endDate','endYn')

class tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = ('number', 'tagname', 'fontcolor', 'bgcolor', 'createDate')
