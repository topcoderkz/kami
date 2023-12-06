from django.urls import path
from .views import AirplaneListCreateView, AirplaneRetrieveUpdateDestroyView

urlpatterns = [
    path('airplanes/', AirplaneListCreateView.as_view(), name='airplane-list-create'),
    path('airplanes/<int:pk>/', AirplaneRetrieveUpdateDestroyView.as_view(), name='airplane-detail-update'),
]
