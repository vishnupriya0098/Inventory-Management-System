from django.urls import path
from .views import create_item, read_item, update_item, delete_item
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('items/', create_item, name='create_item'),
    path('items/<int:item_id>/', read_item, name='read_item'),
    path('update_item/<int:item_id>/', update_item, name='update_item'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain JWT token
    # path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]