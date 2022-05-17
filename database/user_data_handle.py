from pymysql import err
from database import user_data
from flask_bcrypt import Bcrypt


def find_user_info(id):
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


def create_user_info(id, password, store_id=None):
    bcrypt = Bcrypt()
    password_hash = bcrypt.generate_password_hash(password)  # password hashing

    # 스토어 생성부터

    if find_user_info(id=id):  # ID 중복 체크
        user_data.insert_user_info(id=id, password=password_hash, )
