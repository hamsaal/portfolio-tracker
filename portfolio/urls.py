from rest_framework.routers import DefaultRouter
from .views import AssetViewSet, TransactionViewSet

router = DefaultRouter()
router.register('assets', AssetViewSet)
router.register('transactions', TransactionViewSet)

urlpatterns = router.urls