from database import data_connection
from pypika import Query, Table


def get_user_info(id):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    basic_user_info = Table('basicUserInfo')
    query = Query.from_(basic_user_info).select('*').where(basic_user_info.id == id)
    sql = query.get_sql().replace('"', '')
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    test_db.close()

    return result


def insert_user_info(id, password, store_id=None):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    basic_user_info = Table('basicUserInfo')

    if store_id:
        query = Query.into(basic_user_info).columns('id', 'password', 'store_id').insert(id, password, store_id)
    else:
        query = Query.into(basic_user_info).columns('id', 'password').insert(id, password)

    sql = query.get_sql().replace('"', '')
    print(sql)
    cursor.execute(sql)
    test_db.commit()

    cursor.close()
    test_db.close()


def update_user_info(id, changed_password=None, changed_store_id=None):
    # id cannot be changed

    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    update_data = []

    if changed_password:
        update_data.append(['password', changed_password])
    if changed_store_id:
        update_data.append(['store_id', changed_store_id])

    basic_user_info = Table('basicUserInfo')

    for data in update_data:
        query = Query.update(basic_user_info).set(data[0], data[1]).where(basic_user_info.id == id)
        sql = query.get_sql().replace('"', '')
        print(sql)
        cursor.execute(sql)

    test_db.commit()

    cursor.close()
    test_db.close()

    return True
