import csv
import os

from management.api_osm_manager import ApiOsmManager


class ShopManager:
    """
    """
    def __init__(self):
        self.manager = ApiOsmManager()
        self.shops = []
        self.valid_shops = []

    def get_shop(self, feature):
        self.manager._get_request("shop", "all","92150")

    def filter_raw_json(self, raw_json):
        """ method that filters items having all wanted key populated. Items
        are stored in "osm_bicycle_parking" dict variable.
        """
        timestamp = self.__get_timestamp(raw_json)
        for items in self.__get_item(raw_json, 'elements'):
            shop = {}
            tags =  self.__get_item(items, 'tags')
            shop['origin_id'] = self.__get_item(items, 'id')
            shop['timestamp'] = timestamp
            shop['geom_type'] = self.__get_item(items, 'type')
            shop['feature'] = self.__get_item(tags, 'shop')
            shop['name'] = self.__get_item(tags, 'name')
            shop['brand'] = self.__get_item(tags, 'brand')
            shop['operator'] = self.__get_item(tags, 'operator')
            shop['opening_hours'] = self.__get_item(tags, 'opening_hours')
            shop['wheelchair'] = self.__get_item(tags, 'wheelchair')
            shop['housenumber'] = self.__get_item(tags, 'addr:housenumber')
            shop['street'] = self.__get_item(tags, 'addr:street')
            shop['postcode'] = self.__get_item(tags, 'addr:postcode')
            shop['lat'] = self.__get_item(items, 'lat')
            shop['lon'] = self.__get_item(items, 'lon')
            self.shops.append(shop)

    def __get_timestamp(self, raw_json):
         items = self.__get_item(raw_json, 'osm3s')
         return self.__get_item(items, 'timestamp_osm_base')

    def __get_item(self, *args):
        return args[0].get(args[1], None)

    def validity_check(self, shops):
        for item in shops:
            if (
                item['geom_type'] and 
                item['feature'] and 
                item['name'] and
                item['lat'] and
                item['lon'] and
                item['origin_id'] and
                item['timestamp']
            ):
                self.valid_shops.append(item)

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
                "brand",
                "operator",
                "opening_hours",
                "wheelchair",
                "housenumber",
                "street",
                "postcode",
                "lat",
                "lon",
                ]
            )
            for shop in data:
                filewriter.writerow(
                    [
                        shop['origin_id'],
                        shop['timestamp'],
                        shop['geom_type'],
                        shop['feature'],
                        shop['name'],
                        shop['brand'],
                        shop['operator'],
                        shop['opening_hours'],
                        shop['wheelchair'],
                        shop['housenumber'],
                        shop['street'],
                        shop['postcode'],
                        shop['lat'],
                        shop['lon'],
                    ]
                )
