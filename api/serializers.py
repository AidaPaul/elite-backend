from rest_framework import serializers
from api.models import *


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category


class CommoditySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commodity


class EconomySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Economy


class FactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faction


class GovernmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Government


class AllegianceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allegiance


class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State


class SecuritySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Security


class SystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = System


class StationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StationType


class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing



