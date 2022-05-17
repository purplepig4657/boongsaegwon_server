from pymysql import err

from database import store_data
from database.data_validation import utf8len, data_len


def find_store(name=None, store_id=None):
    try:
        result = []
        if store_id is not None:
            result = store_data.get_store_info_by_store_id(store_id=store_id)
        elif name is not None:
            result = store_data.get_store_info_by_name(name=name)
    except Exception as error:
        print(error.__class__)
        if error.__class__ == err.ProgrammingError:
            print("EXCEPTION: programming logic error -> not only code logic, also database table etc...")
            return "ProgrammingError"
        elif error.__class__ == err.OperationalError:
            print("EXCEPTION: check the connection or mysql server, and executed sql.")
            return "OperationalError"
        elif error.__class__ == err.InterfaceError:
            print("EXCEPTION: check the sql query -> maybe there is a query value error.")
            return "InterfaceError"
        else:
            print(error)
            return str(error.__class__)

    if len(result) == 0:
        return None
    else:
        return result[0]


def create_store(name, store_name, category, store_description=None,
                 store_open_info=None, store_photo=None, menu_info=None):
    if name is not None and data_len['name'] < utf8len(name):
        print(f"EXCEPTION: name is too long, have to be under {data_len['name']} bytes")
        return "TooLongName"
    if store_name is not None and data_len['store_name'] < utf8len(store_name):
        print(f"EXCEPTION: store_name is too long, have to be under {data_len['store_name']} bytes")
        return "TooLongStoreName"
    if category is not None and data_len['category'] < utf8len(category):
        print(f"EXCEPTION: category is too long, have to be under {data_len['category']} bytes")
        return "TooLongCategory"
    if store_description is not None and data_len['store_description'] < utf8len(store_description):
        print(f"EXCEPTION: store_description is too long, have to be under {data_len['store_description']} bytes")
        return "TooLongStoreDescription"

    try:
        store_data.insert_store_info(name=name, store_name=store_name, category=category,
                                     store_description=store_description, store_open_info=store_open_info,
                                     store_photo=store_photo, menu_info=menu_info)
    except Exception as error:
        print(error.__class__)
        if error.__class__ == err.ProgrammingError:
            print("EXCEPTION: programming logic error -> not only code logic, also database table etc...")
            return "ProgrammingError"
        elif error.__class__ == err.OperationalError:
            print("EXCEPTION: check the connection or mysql server, and executed sql.")
            return "OperationalError"
        elif error.__class__ == err.InterfaceError:
            print("EXCEPTION: check the sql query -> maybe there is a query value error.")
            return "InterfaceError"
        else:
            print(error)
            return str(error.__class__)

    return True


def update_store(store_id, name=None, store_name=None, category=None, store_description=None,
                 store_open_info=None, store_photo=None, menu_info=None):
    if type(store_id) != int:
        print(f"EXCEPTION: store_id type is int")
        return "TypeError"
    if name is not None and data_len['name'] < utf8len(name):
        print(f"EXCEPTION: name is too long, have to be under {data_len['name']} bytes")
        return "TooLongName"
    if store_name is not None and data_len['store_name'] < utf8len(store_name):
        print(f"EXCEPTION: store_name is too long, have to be under {data_len['store_name']} bytes")
        return "TooLongStoreName"
    if category is not None and data_len['category'] < utf8len(category):
        print(f"EXCEPTION: category is too long, have to be under {data_len['category']} bytes")
        return "TooLongCategory"
    if store_description is not None and data_len['store_description'] < utf8len(store_description):
        print(f"EXCEPTION: store_description is too long, have to be under {data_len['store_description']} bytes")
        return "TooLongStoreDescription"

    try:
        store_data.update_store_info(store_id=store_id, name=name, store_name=store_name, category=category,
                                     store_description=store_description, store_open_info=store_open_info,
                                     store_photo=store_photo, menu_info=menu_info)
    except Exception as error:
        print(error.__class__)
        if error.__class__ == err.ProgrammingError:
            print("EXCEPTION: programming logic error -> not only code logic, also database table etc...")
            return "ProgrammingError"
        elif error.__class__ == err.OperationalError:
            print("EXCEPTION: check the connection or mysql server, and executed sql.")
            return "OperationalError"
        elif error.__class__ == err.InterfaceError:
            print("EXCEPTION: check the sql query -> maybe there is a query value error.")
            return "InterfaceError"
        else:
            print(error)
            return str(error.__class__)

    return True
