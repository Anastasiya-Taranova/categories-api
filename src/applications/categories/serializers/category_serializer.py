from rest_framework import serializers

from applications.categories.models import Category
from applications.categories.serializers.sub_category_serializer import SubCategorySerializer


class CategorySerializer(serializers.ModelSerializer):

    children = serializers.SerializerMethodField('get_children')
    parents = serializers.SerializerMethodField('get_parents')
    siblings = serializers.SerializerMethodField('get_siblings')

    class Meta:
        model = Category
        fields = ('id', 'name', 'children', 'parents', 'siblings',)


    def get_children(self, obj):
        children = obj.get_children()
        serializer = SubCategorySerializer(instance=children, many=True)
        return serializer.data

    def get_parents(self, obj):
        parents = obj.get_parents()
        serializer = SubCategorySerializer(instance=parents, many=True)
        return serializer.data

    def get_siblings(self, obj):
        siblings = obj.get_siblings()
        serializer = SubCategorySerializer(instance=siblings, many=True)
        return serializer.data