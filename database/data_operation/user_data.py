from pypika import Query, Table

from database import data_connection


def get_user_info(id):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    basic_user_info = Table('basicUserInfo')
    query = Query.from_(basic_user_info).select('*').where(basic_user_info.id == id)
    sql = query.get_sql()
    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    test_db.close()

    return result


def insert_user_info(id, password, store_id=None, token=None):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    basic_user_info = Table('basicUserInfo')

    insert_column = []
    insert_data = []

    if id:
        insert_column.append("id")
        insert_data.append(id)
    if password:
        insert_column.append("password")
        insert_data.append(password)
    if store_id:
        insert_column.append("store_id")
        insert_data.append(store_id)
    if token:
        insert_column.append("token")
        insert_data.append(token)

    query = Query.into(basic_user_info).columns(*insert_column).insert(*insert_data)

    sql = query.get_sql()
    cursor.execute(sql)
    test_db.commit()

    cursor.close()
    test_db.close()


def update_user_info(id, password=None, store_id=None, token=None):
    # id cannot be changed

    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    update_data = []

    if password:
        update_data.append(['password', password])
    if store_id:
        update_data.append(['store_id', store_id])
    if token:
        update_data.append(['token', token])

    basic_user_info = Table('basicUserInfo')

    for data in update_data:
        query = Query.update(basic_user_info).set(data[0], data[1]).where(basic_user_info.id == id)
        sql = query.get_sql()
        cursor.execute(sql)

    test_db.commit()

    cursor.close()
    test_db.close()
