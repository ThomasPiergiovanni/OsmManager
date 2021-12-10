import csv
import os

from geojson import LineString, Feature, FeatureCollection, dump

from management.api_osm_manager import ApiOsmManager


class TagManager:
    """
    """
    def __init__(self):
        self.manager = ApiOsmManager()
        self.valid_features = []

    def get_tag(self, overpass_querry):
        self.manager._get_request(overpass_querry)

    def _get_timestamp(self, raw_json):
         items = self._get_item(raw_json, 'osm3s')
         return self._get_item(items, 'timestamp_osm_base')

    def _get_item(self, *args):
        return args[0].get(args[1], None)

    def point_validity_check(self, features):
        for item in features:
            if (
                item['geom_type'] and 
                item['feature'] and 
                item['lat'] and
                item['lon'] and
                item['origin_id'] and
                item['timestamp']
            ):
                self.valid_features.append(item)

    def line_validity_check(self, features):
        for item in features:
            if (
                item['geom_type'] and 
                item['tag_value'] and 
                item['geometry'][0] and
                item['origin_id'] and
                item['timestamp']
            ):
                self.valid_features.append(item)

    def _make_geojson_line(self, item):
        tuple_list = []
        geometry = item['geometry']
        for node in geometry:
            coordinate_tuple = (node['lon'], node['lat'])
            tuple_list.append(coordinate_tuple)
        line = LineString(tuple_list)
        return line


