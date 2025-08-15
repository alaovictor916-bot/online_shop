from django.urls import path
from . views import search_view , product_detail_view , cart_view , seller_view

urlpatterns = [path('products/' , search_view , name= 'search' ) ,
               path('products/<int:id>/' , product_detail_view , name = 'detail_view') ,
               path('cart/<int:id>/' , cart_view , name ='cart') ,
               path('sell/' ,seller_view, name='sell_p' )
]