import csv
import os

from geojson import Point, Feature, FeatureCollection, dump

from controller.tag_manager import TagManager
from management.api_osm_manager import ApiOsmManager


class BusStopManager(TagManager):
    """
    """
    def __init__(self):
        super().__init__()
        self.bus_stop_querry = self.set_overpass_querry
        self.bus_stops = []

    @property
    def set_overpass_querry(self):
        return """
            [timeout:900]
            [out:json];
            area["postal_code"="92150"][admin_level=8];
            node["highway"="bus_stop"](area)->.feature;
            (
                .feature;
            )->.all;
            (.all;);
            out geom;
        """

    def filter_raw_json(self, raw_json):
        """ method that filters items having all wanted key populated. Items
        are stored in "osm_bicycle_parking" dict variable.
        """
        timestamp = self._get_timestamp(raw_json)
        for items in self._get_item(raw_json, 'elements'):
            bus_stop = {}
            tags =  self._get_item(items, 'tags')
            bus_stop['origin_id'] = self._get_item(items, 'id')
            bus_stop['timestamp'] = timestamp
            bus_stop['geom_type'] = self._get_item(items, 'type')
            bus_stop['feature'] = self._get_item(tags, 'highway')
            bus_stop['name'] = self._get_item(tags, 'name')
            bus_stop['shelter'] = self._get_item(tags, 'shelter')
            bus_stop['bench'] = self._get_item(tags, 'bench')
            bus_stop['wheelchair'] = self._get_item(tags, 'wheelchair')
            bus_stop['tactile_paving'] = self._get_item(tags, 'tactile_paving')
            bus_stop['route_ref'] = self._get_item(tags, 'route_ref')
            bus_stop['lat'] = self._get_item(items, 'lat')
            bus_stop['lon'] = self._get_item(items, 'lon')
            self.bus_stops.append(bus_stop)


    def export_geojson(self, path_to_file, filename, data):
        """
        """
        feature_collection = self.__create_feature_collection(data)
        data_file = os.path.join(path_to_file, filename)
        with open(data_file, 'w', encoding='utf8') as file:
            dump(feature_collection, file)

    def __create_feature_collection(self, data):
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
        return FeatureCollection(features)
