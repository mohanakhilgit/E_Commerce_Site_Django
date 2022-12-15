from django.urls import path
from . import views


app_name = 'website'


urlpatterns = [
    path('', views.all_prod_cat, name='home'),
    path('category/<slug:cat_slug>/', views.all_prod_cat, name='products_by_category'),
    path('category/<slug:cat_slug>/<slug:prod_slug>/', views.product_detail, name='product_detail'),
]
