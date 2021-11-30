""" OSm Overapss API manager module.
"""
import requests


class ApiOsmManager:
    """ Api OSM manager class.
    """
    def __init__(self):
        self.response = None
        self.response_json = {}
    
    def _get_request(self, feature, postal_code):
        """ Method that makes a request to OSM API to get 
        peoples' count per transport mode.
        """
        endpoint = self.__set_endpoint()
        header = {}
        overpass_querry = """
            [timeout:900]
            [out:json];
            area["postal_code"=""" + postal_code + """][admin_level=8];
            node["amenity"~""" + feature + """](area)->.feature;
            (
                .feature;
            )->.all;
            (.all;);
            out geom;
        """
        params={'data':overpass_querry}
        response = requests.get(endpoint, headers=header, params=params, verify=False)
        self.response = response
        self.response_json = response.json()
    
    def __set_endpoint(self):

        endpoint = (
            f'https://lz4.overpass-api.de/api/interpreter'
            # f'https://overpass.openstreetmap.fr/api/interpreter'
            # 'https://overpass.kumi.systems/api/interpreter'
        )
        return endpoint
