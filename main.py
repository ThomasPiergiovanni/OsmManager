from controller.shop_manager import ShopManager


if __name__ == "__main__":
    shop = ShopManager()
    shop.get_shop("all")
    shop.filter_raw_json(shop.manager.response_json)
    shop.validity_check(shop.shops)
    counter = 0
    for item in shop.valid_shops:
        print(item)
        counter += 1 
    print(counter)