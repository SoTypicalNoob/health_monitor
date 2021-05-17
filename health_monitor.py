#!/usr/bin/env python3
"""Healht monitor"""

import sys
import sqlite3
import datetime


def create_database(file):
    """function to create database"""
    conn = sqlite3.connect(file)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS BloodPressure")
    cur.execute("DROP TABLE IF EXISTS Scale")

    cur.execute("""CREATE TABLE BloodPressure (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        date DATE,
        systolic INTEGER,
        diastolic INTEGER,
        pulse INTEGER)""")

    # TBW: Body Water Content
    cur.execute("""CREATE TABLE Scale (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        date DATE,
        weight REAL,
        fat REAL,
        tbw REAL,
        mus REAL,
        bone REAL)""")


def add_new_blpressure(filename,
                       date,
                       systolic,
                       diastolic,
                       pulse):
    """Add new blood pressure measurement to the database.

    Arg:
        filename: sqlite database
        date: date and time of the measurement
        systolic: Sys result of the measurement
        diastolic: Dia result of the measurement
        pulse: Pulse

    Returns:
        None.
    """
    connect = sqlite3.connect(filename)
    cursor = connect.cursor()
    cursor.execute("INSERT INTO BloodPressure (date, systolic, diastolic, pulse) VALUES (?, ?, ?, ?)",
                   (date, systolic, diastolic, pulse))

    connect.commit()


def add_new_scalemsr(filename,
                     date,
                     weight,
                     fat,
                     tbw,
                     mus,
                     bone):
    """Add new measurement of scale to the database.

    Arg:
        filename: sqlite database
        date: date and time of the measurement
        weight: weight in kg
        fat: body fat content in %
        tbw: body water content in %
        mus: muscle content in %
        bone: bone weight in kg

    Returns:
        None.
    """
    connect = sqlite3.connect(filename)
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Scale (date, weight, fat, tbw, mus, bone) VALUES (?, ?, ?, ?, ?, ?)",
                   (date, weight, fat, tbw, mus, bone))

    connect.commit()


def main(filename):
    """Main function"""
    now = datetime.datetime.now()
#    systolic = input("Enter Systolic blood pressure [mmHg]: ")
#    diastolic = input("Enter Diastolic blood pressure [mmHg]: ")
#    pulse = input("Enter pulse [BPM]: ")
#    add_new_blpressure(filename,
#                       now.strftime('%Y-%m-%d %H:%M'),
#                       systolic,
#                       diastolic,
#                       pulse)
    weight = input("Enter weight [kg]: ")
    fat = input("Enter body fat content [%]: ")
    tbw = input("Enter body water content [%]: ")
    mus = input("Enter muscle content [%]: ")
    bone = input("Enter bone weight [kg]: ")
    add_new_scalemsr(filename,
                     now.strftime('%Y-%m-%d %H:%M'),
                     weight,
                     fat,
                     tbw,
                     mus,
                     bone)


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        print("Usage: health_monitor.py <filename>")
