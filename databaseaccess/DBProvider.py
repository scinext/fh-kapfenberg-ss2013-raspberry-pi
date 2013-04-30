import sqlite3
import os

def getDBFilepath():
    return os.path.dirname(__file__)+os.sep+"sensordb.sqlite"

def getDBConncetion():
    return sqlite3.connect(getDBFilepath())
