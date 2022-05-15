from database import data_connection


def get_user_info(id):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    sql = f"SELECT * FROM basicUserInfo WHERE id = \"{id}\";"
    cursor.execute(sql)
    result = cursor.fetchall()

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

    cursor.execute(sql)
    test_db.commit()

    cursor.close()
    test_db.close()
