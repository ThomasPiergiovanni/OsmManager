""" OSm Overapss API manager module.
"""
import requests


class ApiOsmManager:
    """ Api OSM manager class.
    """
    def __init__(self):
        self.response = None
        self.response_json = {}
    
    def _get_request(self, tag, feature, postal_code):
        """ Method that makes a request to OSM API to get 
        peoples' count per transport mode.
        """
        endpoint = self.__set_endpoint()
        header = {}
        if tag == "highway" and feature == "cycleway":
            overpass_querry = self.__set_line_querry(tag, feature, postal_code)
        if tag == "bicycle":
            overpass_querry = self.__set_line_querry(tag, feature, postal_code)
        # else:
        #     overpass_querry = self.__set_querry(tag, feature, postal_code)
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
    
    def __set_querry(self, tag, feature, postal_code):
        overpass_querry = None
        if feature == "all":
            overpass_querry = """
                [timeout:900]
                [out:json];
                area["postal_code"=""" + postal_code + """][admin_level=8];
                node[""" + tag + """](area)->.feature;
                (
                    .feature;
                )->.all;
                (.all;);
                out geom;
            """
        else:
            overpass_querry = """
                [timeout:900]
                [out:json];
                area["postal_code"=""" + postal_code + """][admin_level=8];
                node[""" + tag + """~""" + feature + """](area)->.feature;
                (
                    .feature;
                )->.all;
                (.all;);
                out geom;
            """
        return overpass_querry

    def __set_line_querry(self, tag, feature, postal_code):
        overpass_querry = None
        if feature == "all":
            overpass_querry = """
                [timeout:900]
                [out:json];
                area["postal_code"=""" + postal_code + """][admin_level=8];
                way[""" + tag + """](area)->.feature;
                (
                    .feature;
                )->.all;
                (.all;);
                out geom;
            """
        else:
            overpass_querry = """
                [timeout:900]
                [out:json];
                area["postal_code"=""" + postal_code + """][admin_level=8];
                way[""" + tag + """~""" + feature + """](area)->.feature;
                (
                    .feature;
                )->.all;
                (.all;);
                out geom;
            """
        return overpass_querry


