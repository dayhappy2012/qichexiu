from qichexiu.settings import BASE_DIR
import json

from car.models import CarList


def main():
    json_file = BASE_DIR + '/car' + '/car1.json'
    with open(json_file) as f:
        json_str = f.read()
        json_data = json.loads(json_str)
        for item in json_data:

            permission = CarList()
            permission.car_brand = item['car_brand']
            permission.car_icon = item['car_icon']
            permission.car_model = item['car_model']
            permission.car_quote = item['car_quote']
            permission.save()


if __name__ == '__main__':
    main()
