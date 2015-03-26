from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)


class Commodity(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=50)
    average_price = models.IntegerField(null=True, blank=True)


class Economy(models.Model):
    name = models.CharField(max_length=50)


class Faction(models.Model):
    name = models.CharField(max_length=50, null=True)


class Government(models.Model):
    name = models.CharField(max_length=50, null=True)


class Allegiance(models.Model):
    name = models.CharField(max_length=50, null=True)


class State(models.Model):
    name = models.CharField(max_length=50, null=True)


class Security(models.Model):
    name = models.CharField(max_length=50, null=True)


class System(models.Model):
    name = models.CharField(max_length=255)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    faction = models.ForeignKey(Faction, null=True)
    population = models.CharField(max_length=255, null=True)
    government = models.ForeignKey(Government, null=True)
    allegiance = models.ForeignKey(Allegiance, null=True)
    state = models.ForeignKey(State, null=True)
    security = models.ForeignKey(Security, null=True)
    primary_economy = models.ForeignKey(Economy, null=True)
    needs_permit = models.BooleanField(default=False)
    updated_at = models.DateTimeField()


class StationType(models.Model):
    name = models.CharField(max_length=50, null=True)


class Station(models.Model):
    system = models.ForeignKey(System)
    name = models.CharField(max_length=50)
    max_landing_pad_size = models.CharField(max_length=1, null=True)
    distance_to_star = models.IntegerField(null=True)
    faction = models.ForeignKey(Faction, null=True)
    government = models.ForeignKey(Government, null=True)
    allegiance = models.ForeignKey(Allegiance, null=True)
    state = models.ForeignKey(State, null=True)
    type = models.ForeignKey(StationType, null=True)
    has_blackmarket = models.IntegerField()
    has_commodities = models.IntegerField()
    has_refuel = models.IntegerField()
    has_repair = models.IntegerField()
    has_rearm = models.IntegerField()
    has_outfitting = models.IntegerField()
    has_shipyard = models.IntegerField()
    economies = models.ManyToManyField(Economy)
    prohibited_commodities = models.ManyToManyField(Commodity)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)


class Listing(models.Model):
    station = models.ForeignKey(Station)
    commodity = models.ForeignKey(Commodity)
    supply = models.IntegerField()
    demand = models.IntegerField()
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    collected_at = models.DateTimeField()
    update_count = models.IntegerField()

