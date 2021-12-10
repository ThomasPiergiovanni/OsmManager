import os

from geojson import LineString, Feature, FeatureCollection, dump

from controller.tag_manager import TagManager
from management.api_osm_manager import ApiOsmManager


class CyclewayManager(TagManager):
    """
    """
    def __init__(self):
        super().__init__()
        self.cycleway_querry = self.set_overpass_querry
        self.cycleways = []

    @property
    def set_overpass_querry(self):
        return """
            [timeout:900]
            [out:json];
            area["postal_code"="92150"][admin_level=8];
            way["highway"="cycleway"](area)->.feature;
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
            cycleway = {}
            geometry =  self._get_item(items, 'geometry')
            tags =  self._get_item(items, 'tags')
            cycleway['origin_id'] = self._get_item(items, 'id')
            cycleway['timestamp'] = timestamp
            cycleway['geom_type'] = self._get_item(items, 'type')
            cycleway['tag_value'] = self._get_item(tags, 'highway')
            cycleway['name'] = self._get_item(tags, 'name')
            cycleway['oneway'] = self._get_item(tags, 'oneway')
            cycleway['geometry'] = self._get_item(items, 'geometry')
            self.cycleways.append(cycleway)

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
            line = self._make_geojson_line(item)
            features.append(
                Feature(
                    geometry=line,
                    properties={
                        'origin_id': item['origin_id'],
                        'timestamp': item['timestamp'],
                        'type_geom':item['geom_type'],
                        'valeur_objet': item['tag_value'],
                        'nom': item['name'],
                        'sens_unique': item['oneway'],
                    }
                )
            )
        return FeatureCollection(features)
