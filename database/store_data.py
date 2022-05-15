from pypika import Query, Table
from database import data_connection


def get_store_info(store_id):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    store_table = Table('store')
    query = Query.from_(store_table).select('*').where(store_table.store_id == store_id)
    sql = query.get_sql().replace('"', '')

    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    test_db.close()

    return result


def insert_store_info():
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    store_table = Table('store')
    query = Query.into(store_table).columns('*').where(store_table.store_id == store_id)
    sql = query.get_sql().replace('"', '')

    cursor.close()
    test_db.close()

