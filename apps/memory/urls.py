from django.urls import path 

from .views import MemoryCreate, MemoryDetail


urlpatterns = [
    path('create', MemoryCreate.as_view(), name='memory_create'),
    path('detail/<int:pk>', MemoryDetail.as_view(), name='memory_detail'),
]