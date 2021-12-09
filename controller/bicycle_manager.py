import csv
import os

from geojson import LineString, Feature, FeatureCollection, dump

from management.api_osm_manager import ApiOsmManager


class BicycleManager:
    """
    """
    def __init__(self):
        self.manager = ApiOsmManager()
        self.bicycles = []
        self.valid_bicycles = []

    def get_bicycle(self):
        self.manager._get_request(
            "bicycle",
            "all",
            "92150"
        )

    def filter_raw_json(self, raw_json):
        """ method that filters items having all wanted key populated. Items
        are stored in "osm_bicycle_parking" dict variable.
        """
        timestamp = self.__get_timestamp(raw_json)
        for items in self.__get_item(raw_json, 'elements'):
            bicycle = {}
            geometry =  self.__get_item(items, 'geometry')
            tags =  self.__get_item(items, 'tags')
            bicycle['origin_id'] = self.__get_item(items, 'id')
            bicycle['timestamp'] = timestamp
            bicycle['geom_type'] = self.__get_item(items, 'type')
            bicycle['feature'] = self.__get_item(tags, 'bicycle')
            bicycle['name'] = self.__get_item(tags, 'name')
            bicycle['oneway'] = self.__get_item(tags, 'oneway')
            bicycle['surface'] = self.__get_item(tags, 'surface')
            bicycle['segregated'] = self.__get_item(tags, 'segregated')
            bicycle['geometry'] = self.__get_item(items, 'geometry')
            self.bicycles.append(bicycle)

    def __get_timestamp(self, raw_json):
         items = self.__get_item(raw_json, 'osm3s')
         return self.__get_item(items, 'timestamp_osm_base')

    def __get_item(self, *args):
        return args[0].get(args[1], None)

    def validity_check(self, bicycles):
        for item in bicycles:
            if (
                item['geom_type'] and 
                item['feature'] and 
                item['geometry'][0] and
                item['origin_id'] and
                item['timestamp']
            ):
                self.valid_bicycles.append(item)

    def export_geojson(self, path_to_file, filename, data):
        features = []
        for item in data:
            line = self.__make_geojson_line(item)
            features.append(
                Feature(
                    geometry=line,
                    properties={
                        'origin_id': item['origin_id'],
                        'timestamp': item['timestamp'],
                        'type_geom':item['geom_type'],
                        'type_objet': item['feature'],
                        'nom': item['name'],
                        'sens_unique': item['oneway'],
                        'surface': item['surface'],
                        'site_propre': item['segregated'],

                    }
                )
            )
        feature_collection = FeatureCollection(features)

        data_file = os.path.join(path_to_file, filename)
        with open(data_file, 'w', encoding='utf8') as file:
            dump(feature_collection, file)
    
    def __make_geojson_line(self, item):
        tuple_list = []
        geometry = item['geometry']
        for node in geometry:
            coordinate_tuple = (node['lon'], node['lat'])
            tuple_list.append(coordinate_tuple)
        line = LineString(tuple_list)
        return line


