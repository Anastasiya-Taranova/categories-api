from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from applications.categories.models import Category


class SubCategorySerializer(serializers.ModelSerializer):

    name = serializers.StringRelatedField(
        validators=[UniqueValidator(queryset=Category.objects.all())]
    )

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )
