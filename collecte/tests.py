#!/usr/bin/env python3

from optparse import OptionError
from time import sleep
import paho.mqtt.client as mqtt
from datetime import datetime
from MySQLdb import _mysql
import MySQLdb
from MySQLdb._exceptions import OperationalError
from os.path import exists
from os import remove
import random

try:
    db=MySQLdb.connect("mysql.rt13.lab","root","admin", "temp")
except OperationalError:
    db=MySQLdb.connect("mysql.rt13.lab","root","admin")
    db.query("CREATE DATABASE temp")
    db.query("USE temp")

# On se reconnecte automatiquement
db.ping(True)
db.query("""
CREATE TABLE IF NOT EXISTS temp.sensors (
    id INT NOT NULL AUTO_INCREMENT,
    macaddr VARCHAR(12) NOT NULL,
    piece VARCHAR(50) NOT NULL,
    nom VARCHAR(50),
    UNIQUE (macaddr),
    PRIMARY KEY (id))
""")

db.query("""
CREATE TABLE IF NOT EXISTS temp.sensors_data (
    id INT NOT NULL AUTO_INCREMENT,
    sensor_id INT NOT NULL,
    CONSTRAINT sensorFK
        FOREIGN KEY (sensor_id)
        REFERENCES temp.sensors(id),
    datetime DATETIME NOT NULL,
    temp FLOAT NOT NULL,
    PRIMARY KEY (id))
""")
while True:
    test= db.cursor().execute(f"SELECT id FROM sensors WHERE macaddr='B8A5F3569EFF'")
    print(test)
    sleep(2)