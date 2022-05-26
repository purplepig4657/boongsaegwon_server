import os

import json
import base64
import time
import datetime
import uuid

from database.data_handle.user_data_handle import find_user
from database.data_handle.store_data_handle import find_store, update_store


current_working_directory = os.getcwd()
HOST = "http://localhost:8000"
STORE_IMAGE_PATH = "/static/store_image/"
MENU_IMAGE_PATH = "/static/menu_image/"


def is_base64(string):
    try:
        return base64.b64encode(base64.b64decode(string)).decode('utf-8') == string
    except Exception as error:
        # print(error)
        return False


def base64_decode(b64):
    try:
        return base64.b64decode(b64)
    except Exception as error:
        # print(error)
        return None


def get_current_unix_time():
    now = datetime.datetime.now()
    return time.mktime(now.timetuple())


def file_name_generator(id):
    return id + str(get_current_unix_time()).replace('.', '_') + str(uuid.uuid4())


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

    store_photo_urls = store_photo['photo_urls']

    # print(is_base64("aGVsbG8="))

    for i in range(len(store_photo_urls)):
        photo = store_photo_urls[i]
        if is_base64(photo):
            image_data = base64_decode(photo)
            file_name = file_name_generator(id) + '.png'
            try:
                with open(current_working_directory + STORE_IMAGE_PATH + file_name, 'wb') as f:
                    f.write(image_data)
            except Exception as error:
                print(error)
                return "fileIOError"

            store_photo_urls[i] = HOST + STORE_IMAGE_PATH + file_name

    menu = menu_info['menu']

    for i in range(len(menu_info)):
        photo = menu[i]['photo']
        if is_base64(photo):
            image_data = base64_decode(photo)
            file_name = file_name_generator(id) + '.png'
            try:
                with open(current_working_directory + MENU_IMAGE_PATH + file_name, 'wb') as f:
                    f.write(image_data)
            except Exception as error:
                print(error)
                return "fileIOError"

            menu[i]['photo'] = HOST + MENU_IMAGE_PATH + file_name

    store_open_info = json.dumps(store_open_info)
    store_photo = json.dumps(store_photo)
    menu_info = json.dumps(menu_info)

    update_store(store_id=store_id, name=name, store_name=store_name, category=category,
                 store_description=store_description, store_open_info=store_open_info, store_photo=store_photo,
                 menu_info=menu_info)
