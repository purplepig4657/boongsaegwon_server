data_len = {
    'id': 20,
    'password': 256,
    'name': 20,
    'store_name': 100,
    'category': 20,
    'store_description': 1000,
}


def utf8len(data):
    return len(data.encode('utf-8'))
