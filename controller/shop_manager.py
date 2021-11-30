from management.api_osm_manager import ApiOsmManager


class ShopManager:
    """
    """
    def __init__(self):
        self.manager = ApiOsmManager() 

    def get_shop(self):
        self.manager._get_request(
            "shop",
            "all",
            "92150"
        )
        print(self.manager.response_json)
