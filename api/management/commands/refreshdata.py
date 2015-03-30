"""
Script that fetches data from remote json files into database
"""
import datetime
import logging
from django.core.management.base import BaseCommand, CommandError
import requests
from api.models import Category, Commodity, Economy, Listing, Station, System, Faction, Government, Allegiance, \
    State, Security, StationType


logger = logging.getLogger('refreshdata')


class Command(BaseCommand):
    """
    Refreshdata command, import json data into database
    """
    args = 'Which data you want to refresh. (Commodities, Systems, Stations, Listings)'
    help = 'Refreshes database with data from eddb.io json files'

    def process_commodities(self):
        """
        Actual fetching and parsing of commodities and their categories
        And yes, it is intended that we override each category each time as they might change between imports
        """
        logger.debug('Fetching commodities.json')
        commodities = self._fetch_json('http://eddb.io/archive/v3/commodities.json')

        logger.debug('Processing commodities and categories')
        for commodity in commodities:
            commodity_category = Category(id=commodity['category']['id'],
                                          name=commodity['category']['name'])
            commodity_category.save()
            commodity['category'] = commodity_category
            del (commodity['category_id'])
            new_commodity = Commodity(**commodity)
            new_commodity.save()
        logger.debug('Finished processing commodities and categories')

    def process_systems(self):
        """
        Fetching and parsing the systems
        """
        logger.debug('Fetching systems.json')
        systems = self._fetch_json('http://eddb.io/archive/v3/systems.json')

        logger.debug('Processing systems')
        for system in systems:
            if system['primary_economy'] is not None:
                system['primary_economy'] = Economy.objects.get_or_create(name=system['primary_economy'])[0]
            if system['needs_permit'] is None:
                system['needs_permit'] = False
            system['faction'] = Faction.objects.get_or_create(name=system['faction'])[0]
            system['allegiance'] = Allegiance.objects.get_or_create(name=system['allegiance'])[0]
            system['updated_at'] = datetime.datetime.fromtimestamp(system['updated_at'])
            system['government'] = Government.objects.get_or_create(name=system['government'])[0]
            system['state'] = State.objects.get_or_create(name=system['state'])[0]
            system['security'] = Security.objects.get_or_create(name=system['security'])[0]
            new_system = System(**system)
            new_system.save()
        logger.debug('Finished processing systems')

    def process_stations(self):
        """
        Fetching and parsing stations and listings
        """
        logger.debug('Fetching stations.json')
        stations = self._fetch_json('http://eddb.io/archive/v3/stations.json')

        logger.debug('Processing stations')
        for station in stations:
            economies = None
            prohibited_commodities = None
            del(station['import_commodities'])
            del(station['export_commodities'])
            if len(station['prohibited_commodities']) > 0:
                prohibited_commodities = station['prohibited_commodities']
            del station['prohibited_commodities']
            if len(station['economies']) > 0:
                economies = station['economies']
            del station['economies']
            del station['listings']
            if station['has_blackmarket'] is None:
                station['has_blackmarket'] = False
            if station['has_commodities'] is None:
                station['has_commodities'] = False
            if station['has_refuel'] is None:
                station['has_refuel'] = False
            if station['has_repair'] is None:
                station['has_repair'] = False
            if station['has_rearm'] is None:
                station['has_rearm'] = False
            if station['has_outfitting'] is None:
                station['has_outfitting'] = False
            if station['has_shipyard'] is None:
                station['has_shipyard'] = False
            station['faction'] = Faction.objects.get_or_create(name=station['faction'])[0]
            station['allegiance'] = Allegiance.objects.get_or_create(name=station['allegiance'])[0]
            station['state'] = State.objects.get_or_create(name=station['state'])[0]
            station['updated_at'] = datetime.datetime.fromtimestamp(station['updated_at'])
            station['type'] = StationType.objects.get_or_create(name=station['type'])[0]
            station['government'] = Government.objects.get_or_create(name=station['government'])[0]
            new_station = Station(**station)
            new_station.save()

            if economies:
                for economy in economies:
                    new_station.economies.add(Economy.objects.get_or_create(name=economy)[0])
            if prohibited_commodities:
                for commodity in prohibited_commodities:
                    new_station.prohibited_commodities.add(self._get_commodity(commodity))
        logger.debug('Finished processing stations')

    def process_listings(self):
        """
        Fetching and parsing stations and listings
        """
        logger.debug('Fetching stations.json for listings')
        stations = self._fetch_json('http://eddb.io/archive/v3/stations.json')

        logger.debug('Processing listings')
        for station in stations:
            if station['listings'] is None or len(station['listings']) == 0:
                continue  # Nothing to do here, moving on!
            for listing in station['listings']:
                listing['collected_at'] = datetime.datetime.fromtimestamp(listing['collected_at'])
                new_listings = Listing(**listing)
                new_listings.save()
        logger.debug('Finished processing listings')

    def handle(self, *args, **options):
        """
        For now we just overwrite all entries in the db.
        """
        if len(args) == 0:
            self.process_commodities()
            self.process_systems()
            self.process_stations()
            self.process_listings()
            return

        refresh_types = {"commodities": self.process_commodities,
                         "systems": self.process_systems,
                         "stations": self.process_stations,
                         "listings": self.process_listings
                         }
        for arg in args:
            try:
                refresh_types[arg]()
            except KeyError:
                logger.debug("No such option.")

    @staticmethod
    def _fetch_json(url) -> list:
        """
        Attempts to fetch and return json from given URL.
        @rtype : list
        @param url: URL string pointing to a json file
        """
        fetch_headers = {'Accept-Encoding': 'gzip, deflate, sdch'}
        data = requests.get(url, headers=fetch_headers)
        if data.status_code != 200:
            raise CommandError
        return data.json()

    @staticmethod
    def _get_commodity(commodity) -> Commodity:
        """
        Attempts to fetch existing commodity, or create a new one if not found.

        @rtype : Commodity
        @param commodity: Commodity that we are looking for
        @return: Commodity
        """
        commodity = Commodity.objects.filter(name=commodity)
        if len(commodity) == 1:
            return commodity[0]
        else:
            raise FileNotFoundError
