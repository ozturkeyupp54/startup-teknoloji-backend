from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from . import views
from investor.views import InvestorViewSet

router = DefaultRouter()
router.register(r'', InvestorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
