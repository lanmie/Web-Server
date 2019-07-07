import pymysql
import secret
import config
from models.base_model import SQLModel
from models.test_model import Test


def recreate_table(cursor):
    cursor.execute(Test.sql_create)
    # cursor.execute(User.sql_create)
    # cursor.execute(Session.sql_create)
    # cursor.execute(Weibo.sql_create)
    # cursor.execute(Comment.sql_create)


def recreate_database():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=secret.mysql_password,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    with connection.cursor() as cursor:
        cursor.execute(
            'DROP DATABASE IF EXISTS `{}`'.format(
                config.db_name
            )
        )
        cursor.execute(
            'CREATE DATABASE `{}` DEFAULT CHARACTER SET utf8mb4'.format(
                config.db_name
            )
        )
        cursor.execute('USE `{}`'.format(config.db_name))

        recreate_table(cursor)

    connection.commit()
    connection.close()


def test_data():
    SQLModel.init_db()

    Test.new({})


if __name__ == '__main__':
    recreate_database()
    test_data()
