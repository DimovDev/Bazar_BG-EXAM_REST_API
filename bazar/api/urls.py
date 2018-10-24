# Django viewset
from django.conf.urls import url, include


# registriraj router
from rest_framework.routers import DefaultRouter

from user import views
from api.all_product import views as all_product_views
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)  # ne treba base_name jer Django rest_framework skuzi
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)
router.register('my_products', all_product_views.MyProductViewSet, base_name='my_products')
router.register('category', all_product_views.MyCategoryViewSet, base_name='category')
router.register('all_products', all_product_views.AllProductViewSet, base_name='all_products')



urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    # url('products/', views.product_list),
    # url('products/<int:pk>/', views.product_detail),
    # url('category/', views.category_list),
    # url('category/<int:pk>/', views.category_detail),
    url(r'', include(router.urls)),

]
