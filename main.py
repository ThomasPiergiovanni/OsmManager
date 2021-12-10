from config.settings import (
    OUTPUT_FILE,
    BUS_STOP_GJSON,
    CYCLEWAY_GJSON,
    BICYCLE_GJSON

)
from controller.bicycle_manager import BicycleManager
from controller.bus_stop_manager import BusStopManager
from controller.cycleway_manager import CyclewayManager
from controller.shop_manager import ShopManager

def get_osm_bus_stop():
    bus_stop = BusStopManager()
    bus_stop.get_tag(bus_stop.bus_stop_querry)
    bus_stop.filter_raw_json(bus_stop.manager.response_json)
    bus_stop.point_validity_check(bus_stop.bus_stops)
    bus_stop.export_geojson(
        OUTPUT_FILE,
        BUS_STOP_GJSON,
        bus_stop.valid_features
    )

def get_cycleway():
    cycleway = CyclewayManager()
    cycleway.get_tag(cycleway.cycleway_querry)
    cycleway.filter_raw_json(cycleway.manager.response_json)
    cycleway.line_validity_check(cycleway.cycleways)
    cycleway.export_geojson(
        OUTPUT_FILE,
        CYCLEWAY_GJSON,
        cycleway.valid_features
    )

def get_bicycle():
    bicycle = BicycleManager()
    bicycle.get_tag(bicycle.bicycle_querry)
    bicycle.filter_raw_json(bicycle.manager.response_json)
    bicycle.line_validity_check(bicycle.bicycles)
    bicycle.export_geojson(
        OUTPUT_FILE,
        BICYCLE_GJSON,
        bicycle.valid_features
    )

if __name__ == "__main__":
    get_osm_bus_stop()
    get_cycleway()
    get_bicycle()