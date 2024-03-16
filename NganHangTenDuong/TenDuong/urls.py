from django.urls import path
from . import views

app_name = 'TenDuong'  # Thay 'your_app_name' bằng tên thật của ứng dụng

urlpatterns = [
    path('', views.home, name='home'),  # Đường dẫn cho trang chủ
    path('search/', views.search, name='search'),  # Đường dẫn cho trang tìm kiếm
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),  # Đường dẫn cho trang profile
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('edit-allStreet/', views.edit_allStreet, name='edit_allStreet'),
    path('edit-street/<str:street_name>/', views.edit_search_result, name='edit_search_result'),
    path('street/list/', views.street_list, name='street_list'),  # Đường dẫn cho danh sách tên đường
    path('street/<int:street_id>/', views.street_detail, name='street_detail'),  # Đường dẫn cho chi tiết tên đường
    path('chitiet', views.chitiet, name='chitiet'),  # Đường dẫn cho trang chủ
]
