import logging
import datetime
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np

from database import MySQL

color_map = {
    -1: 'indianred',
    0: 'orange',
    1: 'khaki',
    2: 'lightgreen',
    3: 'paleturquoise',
    4: 'dodgerblue',
    5: 'lightsteelblue',
    6: 'slategray',
    7: 'mediumpurple',
    8: 'hotpink',
    9: 'silver',
}


LOG = logging.getLogger('main')


class MySQLDrawer:
    def __init__(self):
        pass

    def _draw_hist(self, name, data):
        plt.clf()
        plt.title(name)
        plt.grid(axis='y')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        xticks = [_ for _ in data.keys()]
        plt.xticks(np.arange(len(xticks)), xticks, fontsize=7)

        xvalues = [_ for _ in  np.arange(len(xticks))]
        plt.bar(xvalues, data.values())

        plt.show()
        # plt.savefig('./tmp/{0}-{1}.jpg'.format(name, str(datetime.datetime.now())))
        plt.close('all')

    def draw_review_num(self, records, period):
        record_map = {}
        for record in records:
            user = record[22]
            date = record[3]
            if period[0] < date < period[1]:
                if user in record_map:
                    record_map[user] += 1
                else:
                    record_map[user] = 1

        self._draw_hist(
            'Review Num from {0} to {1}'.format(period[0], period[1]),
            record_map)

    def draw_review_require_num(self, records, period):
        record_map = {}
        for record in records:
            user = record[37]
            date = record[35]
            if period[0] < date < period[1]:
                if user in record_map:
                    record_map[user] += 1
                else:
                    record_map[user] = 1

        self._draw_hist(
            'Review Require from {0} to {1}'.format(period[0], period[1]),
            record_map)