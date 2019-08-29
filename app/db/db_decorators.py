from mysql.connector import MySQLConnection


def auto_commit(f):
    def wrapper(*args):
        f(*args)
        conn: MySQLConnection = args[0].dao.conn
        conn.commit()

    return wrapper
