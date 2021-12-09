import pytest

from controller.cycleway_manager import CyclewayManager


@pytest.fixture(name="cycleway_json")
def emulate_cycleway_json():
    raw_json = {
        'version': 0.6,
        'generator': 'Overpass API 0.7.57.1 74a55df1',
        'osm3s': {
            'timestamp_osm_base': '2021-12-09T14:30:56Z',
            'timestamp_areas_base': '2021-12-09T13:46:24Z',
            'copyright': 'The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.'
        },
        'elements': [
            {
                'type': 'way',
                'id': 105601834,
                'bounds': {
                    'minlat': 48.8638217,
                    'minlon': 2.2128167,
                    'maxlat': 48.863829,
                    'maxlon': 2.2128989
                },
                'nodes': [
                    1216015711,
                    5580936639,
                    1216015697
                ],
                'geometry': [
                    {
                        'lat': 48.863829,
                        'lon': 2.2128167
                    },
                    {
                        'lat': 48.8638217,
                        'lon': 2.2128788
                    },
                    {
                        'lat': 48.8638239,
                        'lon': 2.2128989
                    }
                ],
                'tags': {
                    'highway': 'cycleway',
                    'name': 'Boulevard du Maréchal Jean de Lattre de Tassigny',
                    'oneway': 'yes',
                    'surface': 'asphalt'
                }
            }
        ]
    }

    return raw_json


@pytest.fixture(name="cycleways_list")
def emulate_cycleways_list():
    cycleways_list = [
        {
            'origin_id': '105601834',
            'timestamp': '2021-12-09T14:30:56Z',
            'geom_type': 'way',
            'feature': 'cycleway',
            'name': 'Boulevard du Maréchal Jean de Lattre de Tassigny',
            'oneway': 'yes',
            'surface': "asphalt",
            'nodes': [
                    1216015711,
                    5580936639,
                    1216015697
                ],
            'geometry': [
                    {
                        'lat': 48.863829,
                        'lon': 2.2128167
                    },
                    {
                        'lat': 48.8638217,
                        'lon': 2.2128788
                    },
                    {
                        'lat': 48.8638239,
                        'lon': 2.2128989
                    }
                ]
        }
    ]

    return cycleways_list


def test_filter_raw_json(cycleway_json):
    cycleway_manager = CyclewayManager()
    cycleway_manager.filter_raw_json(cycleway_json)
    assert cycleway_manager.cycleways[0]['feature'] == 'cycleway'
    assert cycleway_manager.cycleways[0]['nodes'][1]  == 5580936639
    assert cycleway_manager.cycleways[0]['geometry'][0]['lat']  == 48.863829


def test_get_timestamp(cycleway_json):
    cycleway_manager = CyclewayManager()
    returned = cycleway_manager._CyclewayManager__get_timestamp(cycleway_json)
    assert returned == '2021-12-09T14:30:56Z'


def test_validity_check(cycleways_list):
    cycleway_manager = CyclewayManager()
    cycleway_manager.validity_check(cycleways_list)
    assert cycleway_manager.valid_cycleways[0]['geom_type'] == 'way'
    assert cycleway_manager.valid_cycleways[0]['origin_id'] == '105601834'
    assert (
        cycleway_manager.valid_cycleways[0]['geometry'][0]['lat'] == 48.863829
    )

