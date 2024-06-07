from django.urls import path
import review.views as review_views

urlpatterns = [
    path("", review_views.index_page, name="index_page"),
    path("products/", review_views.product_list, name="product_list"),
    path("products/<int:product_id>", review_views.product_page, name="product_page")
]