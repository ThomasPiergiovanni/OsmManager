import pytest

from controller.shop_manager import ShopManager


@pytest.fixture(name="shop_json")
def emulate_shop_json():
    raw_json = {
        'version': 0.6, 'generator': 'Overpass API 0.7.57.1 74a55df1', 'osm3s': {
            'timestamp_osm_base': '2021-11-30T12:26:52Z',
            'timestamp_areas_base': '2021-11-30T12:04:39Z',
            'copyright': 'The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.'
        },
        'elements': [
            {
                'type': 'node',
                'id': 493809023,
                'lat': 48.8690504,
                'lon': 2.2247396,
                'tags': {
                    'addr:housenumber': '4',
                    'addr:postcode': '92150',
                    'addr:street': 'Rue Jules Ferry',
                    'brand': 'Carrefour Market',
                    'brand:wikidata': 'Q2689639',
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
            },
            {
                'type': 'node',
                'id': 1392799523,
                'lat': 48.8635531,
                'lon': 2.2094012,
                'tags': {
                    'addr:housenumber': '48',
                    'addr:postcode': '92150',
                    'addr:street': 'Avenue Jean Jaurès',
                    'brand': 'Casino',
                    'brand:wikidata': 'Q89029184',
                    'delivery:covid19': 'yes',
                    'description:covid19': 'Vente sur place, livraison (commande sur le site)',
                    'fax': '+33 1 41 44 99 19',
                    'name': 'Casino',
                    'opening_hours': 'Mo-Su 07:00-21:00',
                    'opening_hours:covid19': 'Mo-Sa 07:30-19:30; Su 08:00-20:00',
                    'operator': 'Casino',
                    'phone': '+33 1 41 44 99 10',
                    'shop': 'supermarket',
                    'website': 'https://magasins.supercasino.fr/supermarche/suresnes/CS795',
                    'wheelchair': 'yes'
                }
            },
            {
                'type': 'node',
                'id': 1401455852,
                'lat': 48.8658731,
                'lon': 2.20234,
                'tags': {
                    'brand': 'Lidl',
                    'brand:website': 'http://www.lidl.fr',
                    'brand:wikidata': 'Q151954',
                    'brand:wikipedia': 'en:Lidl',
                    'name': 'Lidl',
                    'opening_hours': 'Mo-Sa 08:30-20:00',
                    'opening_hours:covid19': 'Mo-Sa 08:30-19:00',
                    'operator': 'Lidl',
                    'shop': 'supermarket',
                    'wheelchair': 'limited'
                }
            },
            {
                'type': 'node',
                'id': 1423482169,
                'lat': 48.8816352,
                'lon': 2.2250519,
                'tags': {
                    'name': 'Carrefour Express',
                    'opening_hours': 'Mo-Sa 08:00-18:00; Su 08:00-13:00',
                    'shop': 'supermarket'
                }
            },
            {
                'type': 'node',
                'id': 2295513619,
                'lat': 48.8761369,
                'lon': 2.2319248,
                'tags': {
                    'brand': 'Carrefour Market',
                    'brand:wikidata': 'Q2689639',
                    'brand:wikipedia': 'fr:Carrefour Market',
                    'check_date:opening_hours': '2021-04-25',
                    'description:covid19': 'Sera ouvert le dimanche 29 mars de 10h à 13h. En attente de confirmation du siège pour l’ouverture les dimanches suivants',
                    'name': 'Carrefour Market',
                    'opening_hours': 'Mo-Sa 08:30-21:00; Su 09:00-12:30',
                    'opening_hours:covid19': 'Mo-Sa 10:00-19:00',
                    'operator': 'Carrefour',
                    'shop': 'supermarket',
                    'wheelchair': 'yes'
                }
            },
            {
                'type': 'node',
                'id': 3075147029,
                'lat': 48.8633336,
                'lon': 2.2115571,
                'tags': {
                    'brand': 'Carrefour City',
                    'brand:wikidata': 'Q2940187',
                    'brand:wikipedia': 'fr:Carrefour City',
                    'name': 'Carrefour City',
                    'operator': 'Carrefour City',
                    'shop': 'supermarket',
                    'source': 'Survey',
                    'wheelchair': 'yes'
                }
            },
            {
                'type': 'node',
                'id': 3663527953,
                'lat': 48.8679383,
                'lon': 2.227439,
                'tags': {
                    'brand': 'Monoprix',
                    'brand:wikidata': 'Q3321241',
                    'brand:wikipedia':
                    'fr:Monoprix (France)',
                    'description:covid19': 'Paiements uniquement cartes et chèques',
                    'name': 'Monoprix', 'opening_hours': 'Mo-Sa 08:30-21:00, Su 09:00-13:00',
                    'opening_hours:covid19': 'Mo-Su 08:30-20:00',
                    'shop': 'supermarket',
                    'wheelchair': 'yes'
                }
            },
            {
                'type': 'node',
                'id': 3877278811,
                'lat': 48.8756102,
                'lon': 2.2284295,
                'tags': {
                    'brand': 'U Express',
                    'brand:wikidata': 'Q2529029',
                    'brand:wikipedia': 'fr:Système U',
                    'delivery:covid19': 'yes',
                    'description:covid19': 'Vente sur place, livraison, retrait des commandes (sur le site)',
                    'name': 'U Express', 'opening_hours:covid19': 'Mo-Sa 08:00-21:00; Su 09:00-13:00',
                    'phone': '+33 9 67 25 62 10',
                    'shop': 'supermarket',
                    'source': 'cadastre-dgi-fr source : Direction Générale des Impôts - Cadastre. Mise à jour : 2015',
                    'website': 'https://www.coursesu.com/drive-uexpress-suresnes',
                    'wheelchair': 'yes'
                }
            },
            {
                'type': 'node',
                'id': 3950812703,
                'lat': 48.8725252,
                'lon': 2.2271913, 
                'tags': {
                    'brand': 'Franprix',
                    'brand:wikidata': 'Q2420096',
                    'brand:wikipedia': 'fr:Franprix',
                    'name': 'Franprix',
                    'shop': 'supermarket'
                }
            },
            {
                'type': 'node',
                'id': 7149725546,
                'lat': 48.8650505,
                'lon': 2.21448,
                'tags': {
                    'brand': 'Coccinelle Express',
                    'brand:wikidata': 'Q90020479',
                    'name': 'Coccinelle Express',
                    'opening_hours': 'Mo-Su 08:00-22:00',
                    'shop': 'supermarket'
                }
            },
            {
                'type': 'node',
                'id': 7178996300,
                'lat': 48.8631594,
                'lon': 2.2103246,
                'tags': {
                    'brand': 'Biocoop',
                    'brand:wikidata': 'Q2904039',
                    'brand:wikipedia': 'fr:Biocoop',
                    'contact:phone': '+33 1 85 60 62 12',
                    'name': 'Biocoop',
                    'old_name': "Bio C' Bon",
                    'opening_hours': 'Tu-Sa 10:00-20:00; Su 09:30-12:30',
                    'organic': 'only',
                    'shop': 'supermarket'
                }
            },
            {
                'type': 'node',
                'id': 7340165351,
                'lat': 48.8614795,
                'lon': 2.2221699,
                'tags': {
                    'brand': 'Franprix',
                    'brand:wikidata': 'Q2420096',
                    'brand:wikipedia': 'fr:Franprix',
                    'delivery:covid19': 'no',
                    'name': 'Franprix',
                    'opening_hours:covid19': 'Mo-Su 07:00-21:00',
                    'phone': '+33 1 56 04 12 72',
                    'shop': 'convenience;supermarket',
                    'source': 'cadastre-dgi-fr source : Direction Générale des Impôts - Cadastre. Mise à jour : 2019'
                }
            }
        ]
    }
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
