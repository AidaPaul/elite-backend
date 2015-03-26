from rest_framework import viewsets

from api.serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommodityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Commodity to be viewed or edited.
    """
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer


class EconomyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Economy to be viewed or edited.
    """
    queryset = Economy.objects.all()
    serializer_class = EconomySerializer


class FactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Faction to be viewed or edited.
    """
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer


class GovernmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Government to be viewed or edited.
    """
    queryset = Government.objects.all()
    serializer_class = GovernmentSerializer


class AllegianceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Allegiance to be viewed or edited.
    """
    queryset = Allegiance.objects.all()
    serializer_class = AllegianceSerializer


class StateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows State to be viewed or edited.
    """
    queryset = State.objects.all()
    serializer_class = StateSerializer


class SecurityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Security to be viewed or edited.
    """
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer


class SystemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows System to be viewed or edited.
    """
    queryset = System.objects.all()
    serializer_class = SystemSerializer


class StationTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows StationType to be viewed or edited.
    """
    queryset = StationType.objects.all()
    serializer_class = StationTypeSerializer


class StationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Station to be viewed or edited.
    """
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Listing to be viewed or edited.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

