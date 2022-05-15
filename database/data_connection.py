import pymysql


def connect_to_test():
    test_db = pymysql.connect(
        user='root',
        passwd='',
        host='',
        db='test',
        charset='utf8'
    )

    return test_db


def generate_cursor(db):
    return db.cursor(pymysql.cursors.DictCursor)
