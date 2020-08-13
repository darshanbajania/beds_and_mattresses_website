from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
from . import views

app_name = 'sleeping_beds'

urlpatterns = [
    path('',views.Home_view,name='home'),
    path('products/',views.Product_view,name='Products_view'),
    path('about/',views.About_us_view,name='about'),
    path('cart/',views.Cart_view,name='cart'),
    path('checkout/',views.Checkout_view,name='checkout'),
    path('Order_complete/',views.Order_Checkout_view,name='order_complete'),
    path('login/',views.Login_View, name="login_view"),
    path('register/',views.register_view, name="register_view"),
    path('logout/', LogoutView.as_view(next_page='sleeping_beds:home'),name="logout_url"),
    path('Dashboard/',views.Customer_purchase_details_view, name="customer_details"),
    path('Accounts/',views.Accounts_view, name="account_view"),
    path('Admin_dashboard/',views.Admin_dashboard_view,name="admin_dashboard"),
    path('Admin_customer_details/',views.Admin_customer_details_view, name = "admin_customer_details"),
    path('Admin_customer_detail_update/', views.Admin_products_detail_update_view, name="admin_product_detail_update"),
    path('product_update/',views.Admin_product_update_view,name="product_update"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)