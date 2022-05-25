from database.data_handle.user_data_handle import find_user
from database.data_handle.store_data_handle import find_store, update_store

import json


def get_store_info(store_info):
    id = None
    store_id = None

    try:
        id = store_info['id']
    except KeyError:
        try:
            store_id = store_info['store_id']
        except KeyError:
            return "missingValueError"

    if id is not None:
        user = find_user(id=id)
        if user is None or type(user) == str:
            return "idIsInvalidError"

        store_id = user['store_id']

    store_info = find_store(store_id=store_id)

    if store_info['store_open_info'] is not None:
        store_info['store_open_info'] = json.loads(store_info['store_open_info'])
    if store_info['store_photo'] is not None:
        store_info['store_photo'] = json.loads(store_info['store_photo'])
    if store_info['menu_info'] is not None:
        store_info['menu_info'] = json.loads(store_info['menu_info'])

    if type(store_info) == str:
        return store_info
    else:
        return store_info


def set_store_info(store_info):
    try:
        id = store_info['id']
        name = store_info['name']
        store_name = store_info['store_name']
        category = store_info['category']
        store_description = store_info['store_description']
        store_open_info = store_info['store_open_info']
        store_photo = store_info['store_photo']
        menu_info = store_info['menu_info']
    except KeyError:
        return "missingValueError"

    user = find_user(id=id)
    if user is None or type(user) == str:
        return "idIsInvalidError"

    store_id = user['store_id']

    store_open_info = json.dumps(store_open_info)
    store_photo = json.dumps(store_photo)
    menu_info = json.dumps(menu_info)

    update_store(store_id=store_id, name=name, store_name=store_name, category=category,
                 store_description=store_description, store_open_info=store_open_info, store_photo=store_photo,
                 menu_info=menu_info)
