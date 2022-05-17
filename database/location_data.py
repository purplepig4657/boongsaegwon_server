from pypika import Query, Table

from database import data_connection


def get_location_info(store_id):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    location_table = Table('locationData')
    query = Query.from_(location_table).select('*').where(location_table.store_id == store_id)
    sql = query.get_sql().replace('"', '')

    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    test_db.close()

    return result


def insert_location_info(_id, store_id, store_name, is_open, location):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    location_table = Table('locationData')

    column = ["_id", "store_id", "store_name", "is_open", "location"]
    data = [_id, store_id, store_name, is_open, location]

    insert_column = []
    insert_data = []

    for c, d in zip(column, data):
        if d is not None:
            insert_column.append(c)
            insert_data.append(d)

    query = Query.into(location_table).columns(*insert_column).insert(*insert_data)
    sql = query.get_sql()

    cursor.execute(sql)
    test_db.commit()

    cursor.close()
    test_db.close()


def update_location_info(_id, store_id, store_name, is_open, location):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    location_table = Table('locationData')

    column = ["_id", "store_id", "store_name", "is_open", "location"]
    data = [_id, store_id, store_name, is_open, location]

    for c, d in zip(column, data):
        if d is not None:
            query = Query.update(location_table).set(c, d).where(location_table.store_id == store_id)
            sql = query.get_sql()
            cursor.execute(sql)

    test_db.commit()

    cursor.close()
    test_db.close()