from config.settings import (
    OUTPUT_FILE, OUTPUT_SHOP_FILENAME
)
from controller.bus_stop_manager import BusStopManager
from controller.shop_manager import ShopManager

def get_osm_shops():
    shop = ShopManager()
    shop.get_shop("all")
    shop.filter_raw_json(shop.manager.response_json)
    shop.validity_check(shop.shops)
    shop.export_data(OUTPUT_FILE,OUTPUT_SHOP_FILENAME,shop.valid_shops)

def get_osm_bus_stop():
    bus_stop = BusStopManager()
    bus_stop.get_bus_stop("bus_stop")
    print(bus_stop.manager.response_json)


if __name__ == "__main__":
    get_osm_bus_stop()