import logging
import MySQLdb

LOG = logging.getLogger('main')


class Database:
    def __init__(self):
        self.db = None
        self.dbtype = None
        self.is_connected = False

    def connect(self, user, passwd, host='localhost'):
        raise NotImplementedError

    def changedb(self, dbname):
        raise NotImplementedError

    def tables(self):
        raise NotImplementedError

    def search(self, statement):
        raise NotImplementedError


class MySQL(Database):
    def __init__(self):
        Database.__init__(self)
        self.cursor = None
        self.dbtype = 'MySQL'

    def connect(self, user, passwd, host='localhost', dbname=None):
        LOG.info('connect to MySQL...')
        LOG.info('parameter: \n'
                 'user={0} \n'
                 'passwd={1} \n'
                 'host={2} \n'.format(user, passwd, host))

        self.db = MySQLdb.connect(host=host,
                                  user=user,
                                  passwd=passwd)
        self.cursor = self.db.cursor()
        self.is_connected = True
        LOG.info('connect MySQL success.')

        if dbname is not None:
            self.changedb(dbname)

    def changedb(self, dbname):
        assert self.cursor is not None

        self.cursor.execute('USE ' + dbname)
        LOG.info('use database: ' + dbname)

    def tables(self):
        self.cursor.execute('SHOW TABLES')
        tables = self.cursor.fetchall()
        return tables

    def search(self, statement):
        assert statement.lower().startswith('select')
        self.cursor.execute(statement)
        return self.cursor.fetchall()
