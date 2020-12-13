import requests
import json
import time
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = ''
print("Get Resource...")


def get_resource(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    resp = requests.get(BASE_URL+END_POINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())


# get_resource()   # You May Pass Id Or You May Pass Not id
# time.sleep(5)
# print('Post Request...')


def create_resource():
    new_emp = {
        'e_no': 108,
        'e_name': 'Aryan Baba',
        'e_sal': 4000,
        'e_addr': 'Agra_Cant',

    }
    resp = requests.post(BASE_URL+END_POINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())


# create_resource()
# time.sleep(10)
# print("Update Resource...")


def update_resource(id):
    new_data = {
        'id': id,
        'e_no': 106,
        'e_name': 'Aryan Qureshi',
        'e_sal': 4000,
        'e_addr': 'Agra_Cant'
    }
    resp = requests.put(BASE_URL+END_POINT, data=json.dumps(new_data))
    print(resp.status_code)
    print(resp.json())


update_resource(7)
# time.sleep(15)
# print("Delete Resource...")


def delete_resource(id):
    new_data = {
        'id': id,
    }
    resp = requests.delete(BASE_URL+END_POINT, data=json.dumps(new_data))
    print(resp.status_code)
    print(resp.json())


# delete_resource(8)

# py manage.py dumpdata testapp.Employee --indent 5

