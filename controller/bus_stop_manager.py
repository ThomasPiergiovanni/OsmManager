import csv
import os

from geojson import Point, Feature, FeatureCollection, dump

from management.api_osm_manager import ApiOsmManager


class BusStopManager:
    """
    """
    def __init__(self):
        self.manager = ApiOsmManager()
        self.bus_stops = []
        self.valid_bus_stops = []

    def get_bus_stop(self, feature):
        self.manager._get_request(
            "highway",
            feature,
            "92150"
        )

    def filter_raw_json(self, raw_json):
        """ method that filters items having all wanted key populated. Items
        are stored in "osm_bicycle_parking" dict variable.
        """
        timestamp = self.__get_timestamp(raw_json)
        for items in self.__get_item(raw_json, 'elements'):
            bus_stop = {}
            tags =  self.__get_item(items, 'tags')
            bus_stop['origin_id'] = self.__get_item(items, 'id')
            bus_stop['timestamp'] = timestamp
            bus_stop['geom_type'] = self.__get_item(items, 'type')
            bus_stop['feature'] = self.__get_item(tags, 'highway')
            bus_stop['name'] = self.__get_item(tags, 'name')
            bus_stop['shelter'] = self.__get_item(tags, 'shelter')
            bus_stop['bench'] = self.__get_item(tags, 'bench')
            bus_stop['wheelchair'] = self.__get_item(tags, 'wheelchair')
            bus_stop['tactile_paving'] = self.__get_item(tags, 'tactile_paving')
            bus_stop['route_ref'] = self.__get_item(tags, 'route_ref')
            bus_stop['lat'] = self.__get_item(items, 'lat')
            bus_stop['lon'] = self.__get_item(items, 'lon')
            self.bus_stops.append(bus_stop)

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
                item['lat'] and
                item['lon'] and
                item['origin_id'] and
                item['timestamp']
            ):
                self.valid_bus_stops.append(item)

    def export_data(self, path_to_file, filename, data):
        data_file = os.path.join(path_to_file, filename)
        with open(data_file, 'w', newline='',  encoding='utf8') as file:
            filewriter = csv.writer(
                file, delimiter=';',
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )
            filewriter.writerow([
                "origin_id",
                "timestamp",
                "geom_type",
                "feature",
                "name",
                "shelter",
                "bench",
                "wheelchair",
                "tactile_paving",
                "route_ref",
                "lat",
                "lon"
                ]
            )
            for bus_stop in data:
                filewriter.writerow(
                    [
                        bus_stop['origin_id'],
                        bus_stop['timestamp'],
                        bus_stop['geom_type'],
                        bus_stop['feature'],
                        bus_stop['name'],
                        bus_stop['shelter'],
                        bus_stop['bench'],
                        bus_stop['wheelchair'],
                        bus_stop['tactile_paving'],
                        bus_stop['route_ref'],
                        bus_stop['lat'],
                        bus_stop['lon']
                    ]
                )
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


