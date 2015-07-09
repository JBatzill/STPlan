#! /usr/bin/env python
import sys, os
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(MAIN_DIR, ".."))
#----------------------------------------------------------------------------------------------------------------------


from logger import get_log_db
from database import init_db

print("Create new Database?")
print("!!!  This will delete all existing data !!!")

answer = input("y\\n?: ")

if answer == "y":
    print("Creating new database ...")
    get_log_db().info("Creating new database")
    init_db()
    get_log_db().info("New database created!")
    print("New database created!")
    input()