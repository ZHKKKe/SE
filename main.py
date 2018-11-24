import logging
import datetime

from database import MySQL
from drawer import MySQLDrawer

LOG = logging.getLogger('main')


def run(username, passwd, dbname, host, op):
    mysql = MySQL()
    mysql.connect(username, passwd, host)
    mysql.changedb(dbname)

    drawer = MySQLDrawer()

    opid = op['id']
    if opid == 0:
        sql = 'select * from reviews_review INNER JOIN auth_user ON reviews_review.user_id=auth_user.id;'
        result = mysql.search(sql)
        drawer.draw_review_num(result, op['period'])

    elif opid == 1:
        sql = 'select * from reviews_reviewrequest INNER JOIN auth_user ON auth_user.id=reviews_reviewrequest.submitter_id;'
        result = mysql.search(sql)
        drawer.draw_review_require_num(result, op['period'])

if __name__ == '__main__':

    review_num_operate = {
        'id': 0,
        'period': [datetime.datetime(2018, 10, 25), datetime.datetime(2019, 11, 1)],
    }

    review_num_require_operate = {
        'id': 1,
        'period': [datetime.datetime(2018, 10, 25), datetime.datetime(2019, 11, 1)],
    }

    username = 'root'
    passwd = 'root'
    dbname = 'reviewboard'
    host = 'localhost'
    op = review_num_operate

    run(username, passwd, dbname, host, op)
