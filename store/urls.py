from django.urls import include, path
from rest_framework.routers import SimpleRouter, DefaultRouter
from pprint import pprint

from . import views


# router = SimpleRouter()
router = DefaultRouter()
# NOTE: products = endpoint(url) & name of the view set
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
urlpatterns = router.urls


# urlpatterns = [
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:pk>/', views.ProductDetail.as_view()),
#     path('collections/', views.CollectionList.as_view()),
#     path('collections/<int:pk>/', views.CollectionDetail.as_view(),
#          name='collection-detail'),
# ]
