#!/usr/bin/env python3

import MySQLdb as mysql
import subprocess as sb
import datetime
import random
import json


class DBops:

    def __init__(self):
        conn = mysql.connect('localhost', 'deno101', 'denniz', 'matprog')
        cursor = conn.cursor()
        self.runMigrations()
        self.populatedb(cursor, conn, self.checkLast(cursor))
        # self.populate_routes()
        pass

    def runMigrations(self):
        sb.call(['./manage.py', 'makemigrations', 'accounts'])
        sb.call(['./manage.py', 'makemigrations', 'Safari_sys'])
        sb.call(['./manage.py', 'makemigrations', 'booking'])
        sb.call(['./manage.py', 'migrate'])

    def populatedb(self, cursor, conn, id):
        today = datetime.date.today()
        today = datetime.date(today.year, today.month, today.day - 1)

        with open('Info.json', 'r+') as f:
            json_data = json.load(f)

        str_route = json_data['str_route']
        for rad in range(10):
            try:
                date_obj = datetime.date(today.year, today.month, today.day + 1)
            except ValueError:
                try:
                    date_obj = datetime.date(today.year, today.month + 1, 1)
                except ValueError:
                    date_obj = datetime.date(today.year + 1, 1, 1)

            for route in range(1, 24, 1):
                for rad in range(8):
                    seats = random.randint(3, 15)
                    sec = random.randint(25200, 72000)
                    time = datetime.timedelta(seconds=sec)

                    query = f"INSERT INTO booking_busdata VALUES({id},{route},{seats},'{time}','{date_obj}','{str_route[str(route)]}')"
                    cursor.execute(query)
                    id += 1

            today = date_obj

            conn.commit()

    def checkLast(self, cursor):
        query = 'SELECT * FROM booking_busdata'
        cursor.execute(query)
        data = cursor.fetchall()
        if not data:
            return 1
        else:
            return (data[-1][0]) + 1

    def populate_routes(self):
        dic = {}
        container = {}
        with open('Info.json', 'r+') as f:
            json_data = json.load(f)

            for a in json_data['routes']:
                x = json_data['routes'][a]

                for c in x:
                    key = x[c]
                    key = str(key)

                    value = f'{str(a).title()}-{str(c).title()}'
                    dic[key] = value

            container['str_route'] = dic
            json_data.update(container)

        f = open('Info.json', 'w')
        json.dump(json_data, f)


DBops()
