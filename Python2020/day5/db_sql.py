import sqlite3, os
from mypack.database import Database


def test_custom_class():
    db = Database("./database/mysqlite.db")
    sql = """
    SELECT * FROM student
    WHERE grade = ?
    """
    result = db.execute_select(sql, (2,))

    for student in result:
        print("학생:", student)

if __name__ == '__main__':
    test_custom_class()

