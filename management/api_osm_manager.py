""" OSm Overapss API manager module.
"""
import requests
import time


class ApiOsmManager:
    """ Api OSM manager class.
    """
    def __init__(self):
        self.response = None
        self.response_json = {}
    
    def _get_request(self, overpass_querry):
        """ Method that makes a request to OSM API to get 
        peoples' count per transport mode.
        """
        endpoint = self.__set_endpoint()
        header = {}
        params={'data':overpass_querry}
        response = requests.get(endpoint, headers=header, params=params, verify=False)
        time.sleep(2)
        self.response = response
        self.response_json = response.json()
    
    def __set_endpoint(self):

        endpoint = (
            f'https://lz4.overpass-api.de/api/interpreter'
            # f'https://overpass.openstreetmap.fr/api/interpreter'
            # 'https://overpass.kumi.systems/api/interpreter'
        )
        return endpoint
