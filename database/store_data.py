from database import data_connection
from pypika import Query, Table


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


def insert_store_info(name, store_name, category, store_description=None,
                      store_open_info=None, store_photo=None, menu_info=None):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    store_table = Table('store')

    column = ["name", "store_name", "category", "store_description", "store_open_info", "store_photo", "menu_info"]
    data = [name, store_name, category, store_description, store_open_info, store_photo, menu_info]

    insert_column = []
    insert_data = []

    for c, d in zip(column, data):
        if d is not None:
            insert_column.append(c)
            insert_data.append(d)

    query = Query.into(store_table).columns(*insert_column).insert(*insert_data)
    sql = query.get_sql()

    cursor.execute(sql)
    test_db.commit()

    cursor.close()
    test_db.close()


def update_store_info(store_id, name=None, store_name=None, category=None, store_description=None,
                      store_open_info=None, store_photo=None, menu_info=None):
    # store_id cannot be changed
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    store_table = Table('store')

    column = ["name", "store_name", "category", "store_description", "store_open_info", "store_photo", "menu_info"]
    data = [name, store_name, category, store_description, store_open_info, store_photo, menu_info]

    for c, d in zip(column, data):
        if d is not None:
            query = Query.update(store_table).set(c, d).where(store_table.store_id == store_id)
            sql = query.get_sql()
            cursor.execute(sql)

    test_db.commit()

    cursor.close()
    test_db.close()
