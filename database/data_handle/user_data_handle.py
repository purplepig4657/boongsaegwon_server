from pymysql import err
from flask_bcrypt import Bcrypt

from database.data_operation import user_data
from database.data_handle import store_data_handle
from database.data_validation import utf8len, data_len


def find_user(id):
    try:
        result = user_data.get_user_info(id=id)
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


def create_user(id, password):
    if find_user(id=id) is not None:  # ID Integrity Check
        print(f"EXCEPTION: id is duplicated")
        return "DuplicatedId"
    if id is not None and data_len['id'] < utf8len(id):
        print(f"EXCEPTION: id is too long, have to be under {data_len['id']} bytes")
        return "TooLongId"
    if password is not None and data_len['password'] < utf8len(password):
        print(f"EXCEPTION: password is too long, have to be under {data_len['password']} bytes")
        return "TooLongPassword"

    bcrypt = Bcrypt()
    password_hash = bcrypt.generate_password_hash(password)  # password hashing

    try:
        user_data.insert_user_info(id=id, password=str(password_hash, 'utf-8'))
        saved_data = find_user(id=id)
        store_id = saved_data['_id']
        update_user(id=id, store_id=store_id)
        store_data_handle.create_store(store_id=store_id, name=id, store_name=None, category=None)

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


def update_user(id, password=None, store_id=None):
    if find_user(id=id) is None:  # ID validation Check
        print(f"EXCEPTION: id is invalid")
        return "InvalidId"
    if store_id is not None and type(store_id) != int:
        print(f"EXCEPTION: store_id type is int")
        return "TypeError"
    if password is not None and data_len['password'] < utf8len(password):
        print(f"EXCEPTION: password is too long, have to be under {data_len['password']} bytes")
        return "TooLongPassword"

    try:
        if password is not None:
            bcrypt = Bcrypt()
            password_hash = bcrypt.generate_password_hash(password)  # password hashing
            user_data.update_user_info(id=id, password=str(password_hash, 'utf-8'), store_id=store_id)
        else:
            user_data.update_user_info(id=id, store_id=store_id)

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
