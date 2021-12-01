import pytest

from controller.bus_stop_manager import BusStopManager


@pytest.fixture(name="bus_stop_json")
def emulate_bus_stop_json():
    raw_json = {
        'version': 0.6, 'generator': 'Overpass API 0.7.57.1 74a55df1', 'osm3s': {
            'timestamp_osm_base': '2021-12-01T16:35:38Z', 'timestamp_areas_base': '2021-12-01T16:19:25Z', 'copyright': 'The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.'
        },
        'elements': [
            {
                'type': 'node',
                'id': 317275115,
                'lat': 48.8747438,
                'lon': 2.217829,
                'tags': {
                    'STIF:zone': '3',
                    'bus': 'yes',
                    'highway': 'bus_stop',
                    'name': 'Mont Valérien',
                    'public_transport': 'platform',
                    'ref:FR:STIF': '8023',
                    'ref:FR:STIF:stop_id':'StopPoint:59:4024854',
                    'route_ref': '160;241',
                    'source:wheelchair': 'STIF 2019-01',
                    'wheelchair': 'no'
                }
            },
            {
                'type': 'node',
                'id': 317275220,
                'lat': 48.8750326,
                'lon': 2.217647,
                'tags': {
                    'STIF:zone': '3',
                    'bench': 'yes',
                    'bin': 'no',
                    'bus': 'yes',
                    'highway': 'bus_stop',
                    'name': 'Mont Valérien',
                    'public_transport': 'platform',
                    'ref:FR:STIF': '8022',
                    'ref:FR:STIF:stop_id': 'StopPoint:59:4024853',
                    'route_ref': '160;241',
                    'shelter': 'yes',
                    'source:wheelchair': 'STIF 2019-01',
                    'wheelchair': 'no'
                }
            },
            {
                'type': 'node',
                'id': 416315775,
                'lat': 48.863521,
                'lon': 2.2184485,
                'tags': {
                    'STIF:zone': '3',
                    'bench': 'yes',
                    'bin': 'yes',
                    'bus': 'yes',
                    'highway': 'bus_stop',
                    'name': 'Garibaldi',
                    'public_transport':
                    'platform',
                    'ref:FR:STIF': '39369',
                    'ref:FR:STIF:stop_id': 'StopPoint:59:5251768', 
                    'route_ref': '144;244;N53',
                    'shelter': 'yes',
                    'source:wheelchair':
                    'STIF 2019-01',
                    'tactile_paving': 'no',
                    'wheelchair': 'yes'
                }
            }
        ]
    }
    return raw_json

@pytest.fixture(name="bus_stop_json_item")
def emulate_bus_stop_json_item():
    raw_json_item = {
        'STIF:zone': '3',
        'bench': 'yes',
        'bin': 'yes',
        'bus': 'yes',
        'highway': 'bus_stop',
        'name': 'Garibaldi',
        'public_transport':'platform',
        'ref:FR:STIF': '39369',
        'ref:FR:STIF:stop_id': 'StopPoint:59:5251768', 
        'route_ref': '144;244;N53',
        'shelter': 'yes',
        'source:wheelchair':'STIF 2019-01',
        'tactile_paving': 'no',
        'wheelchair': 'yes'
    }
    return raw_json_item

@pytest.fixture(name="bus_stops_list")
def emulate_bus_stops_list():
    bus_stops_list = [
        {
        'origin_id': '416315775',
        'timestamp': '2021-12-01T16:35:38Z',
        'geom_type': 'node',
        'feature': 'bus_stop',
        'name': 'Garibaldi',
        'shelter': 'yes',
        'bench': 'yes',
        'wheelchair': 'yes',
        'tactile_paving': 'no',
        'route_ref': '144;244;N53',
        'lat': 48.863521,
        'lon': 2.2184485
        }
    ]
    return bus_stops_list


def test_filter_raw_json(bus_stop_json):
    bus_stop_manager = BusStopManager()
    bus_stop_manager.filter_raw_json(bus_stop_json)
    assert bus_stop_manager.bus_stops[0]['name'] == 'Mont Valérien'
    assert bus_stop_manager.bus_stops[2]['name'] == 'Garibaldi'


# def test_get_timestamp(shop_json):
#     shop_manager = ShopManager()
#     returned = shop_manager._ShopManager__get_timestamp(shop_json)
#     assert returned == '2021-11-30T12:26:52Z'

# def test_get_item(shop_json_item):
#     shop_manager = ShopManager()
#     returned = shop_manager._ShopManager__get_item(
#         shop_json_item,
#         'wheelchair'
#     )
#     assert returned == 'yes'

# def test_validity_check(shops_list):
#     shop_manager = ShopManager()
#     returned = shop_manager.validity_check(shops_list)
#     assert returned[0]['geom_type'] == 'node'
#     assert returned[0]['origin_id'] == '3877278811'
#     assert returned[0]['lat'] == 48.8756102
#     assert returned[0]['lon'] == 2.2284295
