from database import data_connection


def get_user_info(id):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    sql = f"SELECT * FROM basicUserInfo WHERE id = \"{id}\";"

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print("error")
        return None

    cursor.close()
    test_db.close()

    return result


def insert_user_info(id, password, store_id=None):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    if store_id:
        sql = f"INSERT INTO basicUserInfo (id, password, store_id) VALUES (\"{id}\", \"{password}\", {store_id});"
    else:
        sql = f"INSERT INTO basicUserInfo (id, password) VALUES (\"{id}\", \"{password}\");"

    try:
        cursor.execute(sql)
        test_db.commit()
    except:
        print("error")
        return False

    cursor.close()
    test_db.close()

    return True


def update_user_info(id, changed_password=None, changed_store_id=None):
    # id cannot be changed

    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    update_data = []

    if changed_password:
        update_data.append(['password', changed_password])
    if changed_store_id:
        update_data.append(['store_id', changed_store_id])

    try:
        for data in update_data:
            sql = f"UPDATE basicUserInfo SET {data[0]} = \"{data[1]}\" WHERE id = \"{id}\""
            cursor.execute(sql)

        test_db.commit()
    except:
        print("error")
        return False

    cursor.close()
    test_db.close()

    return True
