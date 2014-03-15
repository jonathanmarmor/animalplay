# -*- coding: utf-8 -*-

from pymongo import MongoClient
import redis


class Database(object):
    def __init__(self):
        self.mongo_conn = MongoClient('localhost', 27017)
        self.mongo = self.mongo_conn.animalplay
        self.r = redis.Redis()
