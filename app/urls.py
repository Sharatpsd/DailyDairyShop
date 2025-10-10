from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),

    # Category
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'),

    # Product Detail
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    # Contact & About
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    # Cart URLs
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),


    # Wishlist URLs
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),


    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    # Search
    path('search/', views.search, name='search'),

    # Buy Now
    path('buy-now/<int:product_id>/', views.buy_now, name='buy_now'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),

    path('checkout/', views.checkout, name='checkout'),


    path('buy-now/<int:product_id>/', views.buy_now, name='buy_now'),
    path('checkout/<int:order_id>/<str:gateway>/', views.checkout_start, name='checkout_start'),
    path('callbacks/bkash/', views.bkash_callback, name='bkash_callback'),
    path('callbacks/nagad/', views.nagad_callback, name='nagad_callback'),



]
