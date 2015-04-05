from rest_framework import serializers
from api.models import *


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category


class CommoditySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.StringRelatedField(source='category.name')

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


class SystemSerializer(serializers.ModelSerializer):
    faction = serializers.StringRelatedField()
    government = serializers.StringRelatedField()
    allegiance = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    security = serializers.StringRelatedField()
    primary_economy = serializers.StringRelatedField()
    stations = serializers.StringRelatedField(source='station_set.all', many=True)

    class Meta:
        model = System


class StationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StationType


class StationSerializer(serializers.ModelSerializer):
    system = serializers.StringRelatedField()
    faction = serializers.StringRelatedField()
    government = serializers.StringRelatedField()
    allegiance = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    type = serializers.StringRelatedField()
    economies = serializers.StringRelatedField(source='economies.all', many=True)
    prohibited_commodities = serializers.StringRelatedField(source='prohibited_commodities.all', many=True)

    class Meta:
        model = Station


class ListingSerializer(serializers.ModelSerializer):
    station = serializers.StringRelatedField()
    commodity = serializers.StringRelatedField()

    class Meta:
        model = Listing



