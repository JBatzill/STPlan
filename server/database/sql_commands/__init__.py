import os

#constants
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

def __read_command(file):
    with open(MAIN_DIR + file, mode='r') as f:
        return f.read()



#SQL_COMMANDS
SQL_CREATE_DB = __read_command("\\stplan_schema.sql")
SQL_READ_STD = __read_command("\\read_std.sql")





