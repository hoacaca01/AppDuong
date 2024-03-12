from django.contrib import admin
from django.urls import path
from . import views

app_name = 'TenDuong'  # Thay 'your_app_name' bằng tên thật của ứng dụng

urlpatterns = [
    path('', views.home, name='home'),  # Đường dẫn cho trang chủ
    path('search/', views.search, name='search'),  # Đường dẫn cho trang tìm kiếm
    path('profile/', views.user_profile, name='user_profile'),  # Đường dẫn cho trang profile
    path('street/list/', views.street_list, name='street_list'),  # Đường dẫn cho danh sách tên đường
    path('street/<int:street_id>/', views.street_detail, name='street_detail'),  # Đường dẫn cho chi tiết tên đường
    path('chitiet', views.chitiet, name='chitiet'),  # Đường dẫn cho trang chủ
]
