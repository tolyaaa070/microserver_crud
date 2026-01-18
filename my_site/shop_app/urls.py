from django.urls import path , include
from rest_framework import routers
from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.SimpleRouter()

urlpatterns = [
    path('' , include(router.urls)),
    path('category/' , CategoryListViewSets.as_view() , name = 'categories'),
    path('category/<int:pk>/' , CategoryDetailViewSets.as_view() , name = 'category_detail'),
    path('category/<int:pk>/edit/', CategoryEditViewSets.as_view(), name='categories_edit'),
    path('category/create/', CategoryCreateViewSets.as_view(), name='category_create'),

    path('product/', ProductListAPIView.as_view(), name='product'),
    path('product/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('product/<int:pk>/edit/' , ProductEditAPIView.as_view() , name = 'product_edit'),
    path('product/create/' , ProductCreateAPIView.as_view() , name = 'product_create'),

    path('cubcategory/' , SubcategoryListViewSet.as_view() , name = 'subcategory'),
    path('cubcategory/<int:pk>/', SubcategoryDetailViewSet.as_view(), name='subcategory_detail'),
    path('cubcategory/<int:pk>/create/', SubcategoryCreateViewSet.as_view(), name='subcategory'),
    path('cubcategory/<int:pk>/edit/', SubcategoryEditViewSet.as_view(), name='subcategory_detail'),

    path('review/', ReviewsListViewSet.as_view(), name='reviews'),
    path('review/<int:pk>/', ReviewsDetailViewSet.as_view(), name='reviews_detail'),
    path('review/<int:pk>/edit/', ReviewsEditViewSet.as_view(), name='reviews_edit'),
    path('review/create/', ReviewsCreateViewSet.as_view(), name='reviews_create'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]