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


def get_all_location_info():
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    location_table = Table('locationData')
    query = Query.from_(location_table).select('*')
    sql = query.get_sql().replace('"', '')

    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    test_db.close()

    return result


def insert_location_info(store_id, store_name, is_open=None, latitude=None, longitude=None):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    location_table = Table('locationData')

    column = ["store_id", "store_name", "is_open", "latitude", "longitude"]
    data = [store_id, store_name, is_open, latitude, longitude]

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


def update_location_info(store_id, store_name=None, is_open=None, latitude=None, longitude=None):
    # store_id cannot be changed

    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    location_table = Table('locationData')

    column = ["store_name", "is_open", "latitude", "longitude"]
    data = [store_name, is_open, latitude, longitude]

    for c, d in zip(column, data):
        if d is not None:
            query = Query.update(location_table).set(c, d).where(location_table.store_id == store_id)
            sql = query.get_sql()
            cursor.execute(sql)

    test_db.commit()

    cursor.close()
    test_db.close()
