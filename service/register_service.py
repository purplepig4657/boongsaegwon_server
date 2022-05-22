from database.data_handle.user_data_handle import create_user


def register(register_info):
    try:
        id = register_info['id']
        password = register_info['password']
    except KeyError:
        return "missingValueError"

    result = create_user(id=id, password=password)

    if type(result) == str:
        return result
    else:
        return True
