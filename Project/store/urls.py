from django.urls import path
from . import views

urlpatterns = [

        path('', views.store, name="store"),
        path('cart/', views.cart, name="cart"),
        path('checkout/', views.checkout, name="checkout"),
        path('update_item/', views.updateItem, name="update_item"),
        path('detail/<int:id>',views.detail,name='detail'),
        path('profile/', views.profile, name="profile"),
        path('logout_view/', views.logout_view, name="logout_view"),
        path('login/', views.login, name="login"),
        path('register/', views.register, name="register"),
        path('loadproduct/', views.loadproduct, name="loadproduct"),
        path('recommended/', views.recommendedProduct, name="recommended"),
        path('produce/', views.produce, name="produce"),
        path('createdataframe/', views.createDataframe, name="createdataframe"),
]