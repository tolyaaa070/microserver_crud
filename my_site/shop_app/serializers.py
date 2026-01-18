from .models import *
from rest_framework import serializers

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_image' , 'category_name']

class SubCategorySerializers(serializers.ModelSerializer):
    category = CategorySerializers(read_only=True , many= True)
    class Meta:
        model = Subcategory
        fields = ['category' , 'subcat_name']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = [ 'subcat_name']
class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['product_image']

class ReviewsProductSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%d-%m-%y , %H:%M')

    class Meta:
        model = Reviews
        fields = ['user_id', 'text' , 'stars' , 'created']

class ProductListSerializers(serializers.ModelSerializer):

    product_photos = ProductImageSerializers(read_only=True , many= True )
    created = serializers.DateTimeField(format='%d-%m-%y , %H:%M')
    class Meta:
        model = Product
        fields = ['id','category' , 'product_name' , 'owner_id' ,'product_photos', 'article_num' , 'description',
             'product_type'  , 'price' , 'created']

class ProductDetailSerializers(serializers.ModelSerializer):
    product_reviews = ReviewsProductSerializer(read_only=True , many = True)
    product_photos = ProductImageSerializers(read_only=True , many= True )
    sub_category_product = SubCategorySerializer(read_only=True , many = True)
    created = serializers.DateTimeField(format='%d-%m-%y , %H:%M' , read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_reviews= serializers.SerializerMethodField()
    owner_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Product
        fields = ['product_name','product_photos','sub_category_product','owner_id',
                  'created','price','product_type','avg_rating','count_reviews' , 'product_reviews']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_reviews(self, obj):
        return obj.get_count_reviews()

class ReviewsSerializers(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%d-%m-%y , %H:%M', read_only=True )
    user_id = serializers.IntegerField(read_only=True)
    # product = serializers.PrimaryKeyRelatedField(
    #     queryset=Product.objects.all()
    # )

    class Meta:
        model = Reviews
        fields = ['user_id' , 'product' , 'text' , 'stars' , 'created']
