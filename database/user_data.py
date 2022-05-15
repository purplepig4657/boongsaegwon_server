from database import data_connection
from pypika import Query, Table

def get_user_info(id):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)


    basicUserInfo = Table('basicUserInfo')
    sql = Query.from_(basicUserInfo).select('*').where(basicUserInfo.id == id)
    sql = sql.get_sql().replace('"', '')
    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    test_db.close()

    return result


def insert_user_info(id, password, store_id=None):
    test_db = data_connection.connect_to_test()
    cursor = data_connection.generate_cursor(test_db)

    if store_id:
        basicUserInfo = Table('basicUserInfo')
        sql = Query.into(basicUserInfo).columns(
        'id','password','store_id'
        ).insert(
        id,password,store_id
        )

    else:

        basicUserInfo = Table('basicUserInfo')
        sql = Query.into(basicUserInfo).columns(
            'id','password'
        ).insert(
            id,password
        )

    sql = sql.get_sql().replace('"', '')
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

    for data in update_data:

        basicUserInfo = Table('basicUserInfo')
        sql = Query.update(
         basicUserInfo
        ).set(
            data[0], data[1]
        ).where(
            basicUserInfo.id == id
        )
        sql = sql.get_sql().replace('"', '')
        cursor.execute(sql)

    test_db.commit()

    cursor.close()
    test_db.close()

    return True
