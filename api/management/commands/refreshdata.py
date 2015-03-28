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
    args = 'Which data you want to refresh. For now it is ignored'
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
                system['primary_economy'] = self._get_economy(system['primary_economy'])
            if system['needs_permit'] is None:
                system['needs_permit'] = False
            system['faction'] = self._get_faction(system['faction'])
            system['allegiance'] = self._get_allegiance(system['allegiance'])
            system['updated_at'] = datetime.datetime.fromtimestamp(system['updated_at'])
            system['government'] = self._get_government(system['government'])
            system['state'] = self._get_state(system['state'])
            system['security'] = self._get_security(system['security'])
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
            station['faction'] = self._get_faction(station['faction'])
            station['allegiance'] = self._get_allegiance(station['allegiance'])
            station['state'] = self._get_state(station['state'])
            station['updated_at'] = datetime.datetime.fromtimestamp(station['updated_at'])
            station['type'] = self._get_station_type(station['type'])
            station['government'] = self._get_government(station['government'])
            new_station = Station(**station)
            new_station.save()

            if economies:
                for economy in economies:
                    new_station.economies.add(self._get_economy(economy))
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
        self.process_commodities()
        self.process_systems()
        self.process_stations()
        self.process_listings()

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
    def _get_faction(faction) -> Faction:
        """
        Attempts to fetch existing faction, or create a new one if not found.

        @rtype : Faction
        @param faction: Faction that we are looking for
        @return: Faction
        """
        if faction is None or len(faction) == 0:
            faction = 'No faction'
        system_faction = Faction.objects.filter(name=faction)
        if len(system_faction) == 1:
            faction = system_faction[0]
        else:
            new_faction = Faction(name=faction)
            new_faction.save()
            faction = new_faction
        return faction

    @staticmethod
    def _get_economy(economy) -> Economy:
        """
        Attempts to fetch existing economy, or create a new one if not found.

        @rtype : Economy
        @param economy: Economy that we are looking for
        @return: Economy
        """
        entity_economy = Economy.objects.filter(name=economy)
        if len(entity_economy) == 1:
            economy = entity_economy[0]
        else:
            new_economy = Economy(name=economy)
            new_economy.save()
            economy = new_economy
        return economy

    @staticmethod
    def _get_allegiance(allegiance) -> Allegiance:
        """
        Attempts to fetch existing allegiance, or create a new one if not found.

        @rtype : Allegiance
        @param allegiance: Allegiance that we are looking for
        @return: Allegiance
        """
        entity_allegiance = Allegiance.objects.filter(name=allegiance)
        if len(entity_allegiance) == 1:
            allegiance = entity_allegiance[0]
        else:
            new_allegiance = Allegiance(name=allegiance)
            new_allegiance.save()
            allegiance = new_allegiance
        return allegiance

    @staticmethod
    def _get_government(government) -> Government:
        """
        Attempts to fetch existing government, or create a new one if not found.

        @rtype : Government
        @param government: Government that we are looking for
        @return: Government
        """
        entity_government = Government.objects.filter(name=government)
        if len(entity_government) == 1:
            government = entity_government[0]
        else:
            new_government = Government(name=government)
            new_government.save()
            government = new_government
        return government

    @staticmethod
    def _get_state(state) -> State:
        """
        Attempts to fetch existing state, or create a new one if not found.

        @rtype : State
        @param state: State that we are looking for
        @return: State
        """
        entity_state = State.objects.filter(name=state)
        if len(entity_state) == 1:
            state = entity_state[0]
        else:
            new_state = State(name=state)
            new_state.save()
            state = new_state
        return state

    @staticmethod
    def _get_security(security) -> Security:
        """
        Attempts to fetch existing security, or create a new one if not found.

        @rtype : Security
        @param security: Security that we are looking for
        @return: Security
        """
        entity_security = Security.objects.filter(name=security)
        if len(entity_security) == 1:
            security = entity_security[0]
        else:
            new_security = Security(name=security)
            new_security.save()
            security = new_security
        return security

    @staticmethod
    def _get_station_type(stationtype) -> StationType:
        """
        Attempts to fetch existing stationtype, or create a new one if not found.

        @rtype : StationType
        @param stationtype: StationType that we are looking for
        @return: StationType
        """
        entity_stationtype = StationType.objects.filter(name=stationtype)
        if len(entity_stationtype) == 1:
            stationtype = entity_stationtype[0]
        else:
            new_stationtype = StationType(name=stationtype)
            new_stationtype.save()
            stationtype = new_stationtype
        return stationtype

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
