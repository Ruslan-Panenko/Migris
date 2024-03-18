from django.urls import path
from .views import CustomUserListCreate, CustomUserRetrieveUpdateDestroy

urlpatterns = [
    path('', CustomUserListCreate.as_view(), name='user-list'),
    path('<int:pk>/', CustomUserRetrieveUpdateDestroy.as_view(), name='user-detail'),
]
