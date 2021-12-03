import pytest

from controller.cycleway_manager import CyclewayManager


@pytest.fixture(name="cycleway_json")
def emulate_cycleway_json():
    raw_json = {}
    return raw_json

@pytest.fixture(name="shop_json_item")
def emulate_shop_json_item():
    raw_json_item = {
        'addr:housenumber': '4',
        'addr:postcode': '92150',
        'brand:wikipedia': 'fr:Carrefour Market',
        'delivery:covid19': 'yes',
        'description:covid19': 'Livraisons à domicile du lundi au samedi 10h-17h',
        'name': 'Carrefour Market',
        'opening_hours': 'Mo-Sa 08:30-21:00; Su 09:00-13:00',
        'opening_hours:covid19': 'Mo-Sa 10:00-19:00; Su 10:00-12:30',
        'operator': 'Carrefour',
        'shop': 'supermarket',
        'wheelchair': 'yes'
    }
    return raw_json_item

@pytest.fixture(name="shops_list")
def emulate_shops_list():
    shops_list = [
        {
        'origin_id': '3877278811',
        'timestamp': '2021-11-30T12:26:52Z',
        'geom_type': 'node',
        'feature': 'supermarket',
        'name': 'U Express',
        'brand': 'U Express',
        'operator': None,
        'opening_hours': 'Mo-Sa 10:00-19:00; Su 10:00-12:30',
        'wheelchair': 'yes',
        'housenumber': None,
        'street': None,
        'postcode': None,
        'lat': 48.8756102,
        'lon': 2.2284295
        }
    ]

    return shops_list


def test_filter_raw_json(shop_json):
    shop_manager = ShopManager()
    shop_manager.filter_raw_json(shop_json)
    assert shop_manager.shops[0]['name'] == 'Carrefour Market'
    assert shop_manager.shops[1]['name'] == 'Casino'


def test_get_timestamp(shop_json):
    shop_manager = ShopManager()
    returned = shop_manager._ShopManager__get_timestamp(shop_json)
    assert returned == '2021-11-30T12:26:52Z'

def test_get_item(shop_json_item):
    shop_manager = ShopManager()
    returned = shop_manager._ShopManager__get_item(
        shop_json_item,
        'wheelchair'
    )
    assert returned == 'yes'

def test_validity_check(shops_list):
    shop_manager = ShopManager()
    shop_manager.validity_check(shops_list)
    assert shop_manager.valid_shops[0]['geom_type'] == 'node'
    assert shop_manager.valid_shops[0]['geom_type'] == 'node'
    assert shop_manager.valid_shops[0]['origin_id'] == '3877278811'
    assert shop_manager.valid_shops[0]['lat'] == 48.8756102
    assert shop_manager.valid_shops[0]['lon'] == 2.2284295
