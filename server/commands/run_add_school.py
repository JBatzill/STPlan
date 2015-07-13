#! /usr/bin/env python
import sys, os
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(MAIN_DIR, ".."))
#----------------------------------------------------------------------------------------------------------------------


from logger import get_log_db
from database.controller import ctrl_school
import database

print("Adding school ...")
print("Pls answer following question [(*) := optional]:")

name = input("name [2-128]: ")
shortcut = input("shortcut [2-16]: ")
url = input("url: ")
username = input("(username): ")
pw = input("(password): ")
city = input("city [2-32]: ")
state = input("(state) [2-32]: ")
country = input("(country) [2-32]: ")

answer = input("\nadd school y\\n: ")

if answer == "y":
    get_log_db().info("adding school")
    db = database.connect_db()

    try:
        row_id = ctrl_school.add_school(db, name, shortcut, url, city, username, pw, state, country)
        get_log_db().info(name + " added, id: " +str(row_id))
        open(os.path.join(MAIN_DIR, "..", "database", "school.id"), "a+").write(name + ", " + city + ": " + str(row_id) + "\n")
    except ValueError as e:
        print("Error while creating school entry:")
        print(str(e))
        print("Please try again")

    db.close();
    input()