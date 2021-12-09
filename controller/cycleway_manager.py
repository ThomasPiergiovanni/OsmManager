import csv
import os

from geojson import LineString, Feature, FeatureCollection, dump

from management.api_osm_manager import ApiOsmManager


class CyclewayManager:
    """
    """
    def __init__(self):
        self.manager = ApiOsmManager()
        self.cycleways = []
        self.valid_cycleways = []

    def get_cycleway(self):
        self.manager._get_request(
            "highway",
            "cycleway",
            "92150"
        )
        print(self.manager.response_json)

    def filter_raw_json(self, raw_json):
        """ method that filters items having all wanted key populated. Items
        are stored in "osm_bicycle_parking" dict variable.
        """
        timestamp = self.__get_timestamp(raw_json)
        for items in self.__get_item(raw_json, 'elements'):
            cycleway = {}
            nodes =  self.__get_item(items, 'nodes')
            geometry =  self.__get_item(items, 'geometry')
            tags =  self.__get_item(items, 'tags')
            cycleway['origin_id'] = self.__get_item(items, 'id')
            cycleway['timestamp'] = timestamp
            cycleway['geom_type'] = self.__get_item(items, 'type')
            cycleway['feature'] = self.__get_item(tags, 'highway')
            cycleway['name'] = self.__get_item(tags, 'name')
            cycleway['oneway'] = self.__get_item(tags, 'oneway')
            cycleway['surface'] = self.__get_item(tags, 'surface')
            cycleway['nodes'] = self.__get_item(items, 'nodes')
            cycleway['geometry'] = self.__get_item(items, 'geometry')
            self.cycleways.append(cycleway)

    def __get_timestamp(self, raw_json):
         items = self.__get_item(raw_json, 'osm3s')
         return self.__get_item(items, 'timestamp_osm_base')

    def __get_item(self, *args):
        return args[0].get(args[1], None)

    def validity_check(self, bus_stops):
        for item in bus_stops:
            if (
                item['geom_type'] and 
                item['feature'] and 
                item['name'] and
                item['nodes'][0] and
                item['geometry'][0] and
                item['origin_id'] and
                item['timestamp']
            ):
                self.valid_cycleways.append(item)

    def export_geojson(self, path_to_file, filename, data):
        features = []
        for item in data:
            point = Point((item['lon'], item['lat']))
            features.append(
                Feature(
                    geometry=point,
                    properties={
                        'origin_id': item['origin_id'],
                        'timestamp': item['timestamp'],
                        'type_geom':item['geom_type'],
                        'type_objet': item['feature'],
                        'nom': item['name'],
                        'abris': item['shelter'],
                        'banc': item['bench'],
                        'fauteuil_roulant': item['wheelchair'],
                        'route_ref': item['route_ref']

                    }
                )
            )
        feature_collection = FeatureCollection(features)

        data_file = os.path.join(path_to_file, filename)
        with open(data_file, 'w', encoding='utf8') as file:
            dump(feature_collection, file)
