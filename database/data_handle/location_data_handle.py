from pymysql import err

from database.data_operation import location_data


def find_location(store_id):
    try:
        result = location_data.get_location_info(store_id=store_id)
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


def find_all_location():
    try:
        result = location_data.get_all_location_info()
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
        return result


def create_location(store_id, store_name, is_open=None, latitude=None, longitude=None):
    if find_location(store_id=store_id) is not None:  # store_id Integrity Check
        print(f"EXCEPTION: id is duplicated")
        return "DuplicatedId"
    if latitude is not None and type(latitude) != float:
        print(f"EXCEPTION: latitude type should be float")
        return "TypeError"
    if longitude is not None and type(longitude) != float:
        print(f"EXCEPTION: longitude type should be float")
        return "TypeError"

    try:
        if is_open is None:
            is_open = False
        location_data.insert_location_info(store_id=store_id, store_name=store_name, is_open=is_open,
                                           latitude=latitude, longitude=longitude)

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


def update_location(store_id, store_name=None, is_open=None, latitude=None, longitude=None):
    if latitude is not None and type(latitude) != float:
        print(f"EXCEPTION: latitude type should be float")
        return "TypeError"
    if longitude is not None and type(longitude) != float:
        print(f"EXCEPTION: longitude type should be float")
        return "TypeError"

    try:
        if is_open is None:
            is_open = False
        location_data.update_location_info(store_id=store_id, store_name=store_name, is_open=is_open,
                                           latitude=latitude, longitude=longitude)

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
