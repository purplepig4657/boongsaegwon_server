from database.data_handle.user_data_handle import find_user
from database.data_handle.location_data_handle import find_location, find_all_location, update_location


def get_location_info(location_info):
    try:
        store_id = location_info['store_id']
    except KeyError:
        return "missingValueError"

    location_info = find_location(store_id=store_id)

    if type(location_info) == str:
        return location_info
    else:
        return location_info


def get_all_location_info():
    location_all_info = find_all_location()

    if type(location_all_info) == str:
        return location_all_info
    else:
        return location_all_info


def set_location_info(location_info):
    try:
        id = location_info['id']
        is_open = location_info['is_open']
        latitude = location_info['latitude']
        longitude = location_info['longitude']
    except KeyError:
        return "missingValueError"

    user = find_user(id=id)
    if user is None or type(user) == str:
        return "idIsInvalidError"

    store_id = user['store_id']

    update_location(store_id=store_id, is_open=is_open, latitude=latitude, longitude=longitude)
