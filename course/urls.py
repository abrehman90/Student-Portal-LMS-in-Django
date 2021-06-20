from django.urls import path
from .views import *
from django.conf.urls import url


app_name = 'shopping_cart'

urlpatterns = [
    # url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    # url(r'^order-summary/$', order_details, name="order_summary"),
    # url(r'^success/$', success, name='purchase_success'),
    # url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    # url(r'^checkout/$', checkout, name='checkout'),
    # url(r'^update-transaction/(?P<token>[-\w]+)/$', update_transaction_records,
    #     name='update_records'),
    path('',newcourse,name='coursepaid'),
    # path('cart/',cart.as_view(),name='cart'),
    path('courseview/<int:myid>',productView,name='productview'),
]
