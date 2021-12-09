from config.settings import (
    OUTPUT_FILE,
    OUTPUT_SHOP_FILENAME,
    OUTPUT_BUS_STOP_FILENAME,
    BUS_STOP_GJSON,
    CYCLEWAY_GJSON,
    BICYCLE_GJSON

)
from controller.bicycle_manager import BicycleManager
from controller.bus_stop_manager import BusStopManager
from controller.cycleway_manager import CyclewayManager
from controller.shop_manager import ShopManager

def get_osm_shops():
    shop = ShopManager()
    shop.get_shop()
    shop.filter_raw_json(shop.manager.response_json)
    shop.validity_check(shop.shops)
    shop.export_data(OUTPUT_FILE,OUTPUT_SHOP_FILENAME,shop.valid_shops)

def get_osm_bus_stop():
    bus_stop = BusStopManager()
    bus_stop.get_bus_stop()
    bus_stop.filter_raw_json(bus_stop.manager.response_json)
    bus_stop.validity_check(bus_stop.bus_stops)
    bus_stop.export_geojson(
        OUTPUT_FILE,
        BUS_STOP_GJSON,
        bus_stop.valid_bus_stops
    )

def get_cycleway():
    cycleway = CyclewayManager()
    cycleway.get_cycleway()
    cycleway.filter_raw_json(cycleway.manager.response_json)
    cycleway.validity_check(cycleway.cycleways)
    cycleway.export_geojson(
        OUTPUT_FILE,
        CYCLEWAY_GJSON,
        cycleway.valid_cycleways
    )

def get_bicycle():
    bicycle = BicycleManager()
    bicycle.get_bicycle()
    bicycle.filter_raw_json(bicycle.manager.response_json)
    bicycle.validity_check(bicycle.bicycles)
    bicycle.export_geojson(
        OUTPUT_FILE,
        BICYCLE_GJSON,
        bicycle.valid_bicycles
    )

if __name__ == "__main__":
    # get_osm_shops()
    # get_osm_bus_stop()
    get_cycleway()
    get_bicycle()