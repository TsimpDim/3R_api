from rest_framework import routers
from django.urls import path, include
from api.views import ResourceViewSet, RemovedResourceViewSet, OptionRetrieveUpdateView

router = routers.DefaultRouter()
router.register(r'resources', ResourceViewSet)
router.register(r'trash', RemovedResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('options/', OptionRetrieveUpdateView.as_view())
]