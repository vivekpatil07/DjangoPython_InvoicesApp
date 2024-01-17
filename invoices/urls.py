from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailViewSet

router = DefaultRouter()
router.register(r"invoices", InvoiceViewSet, basename="invoices-api-view")
router.register(r"invoices-details", InvoiceDetailViewSet)

urlpatterns = router.urls
