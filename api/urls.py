from django.conf.urls import url, include
from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'commodities', views.CommodityViewSet)
router.register(r'economies', views.EconomyViewSet)
router.register(r'factions', views.FactionViewSet)
router.register(r'governments', views.GovernmentViewSet)
router.register(r'allegiances', views.AllegianceViewSet)
router.register(r'states', views.StateViewSet)
router.register(r'securities', views.SecurityViewSet)
router.register(r'systems', views.SystemViewSet)
router.register(r'station_types', views.StationTypeViewSet)
router.register(r'stations', views.StationViewSet)
router.register(r'listings', views.ListingViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]