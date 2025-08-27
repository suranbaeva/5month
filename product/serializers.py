from rest_framework import serializers
from .models import Product, Review, Category

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Рейтинг должен быть от 1 до 5.")
        return value

    def validate_text(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Отзыв слишком короткий (минимум 10 символов).")
        return value


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 2

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть положительной.")
        return value

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Название должно быть не короче 3 символов.")
        return value

    def validate(self, attrs):
        title = attrs.get('title')
        description = attrs.get('description')
        if title and description and title.lower() in description.lower():
            raise serializers.ValidationError("Описание не должно содержать название.")
        return attrs


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_product_count(self, obj):
        return obj.products.count()

    def get_product_count(self, obj):
        return obj.products.count()

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название не может быть пустым.")


        if self.instance is None and Category.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Категория с таким названием уже существует.")

        return value