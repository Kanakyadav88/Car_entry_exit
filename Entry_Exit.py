# Car entry-exit system:  Managing entry and exit using MySql
#  return -1 when database cannot be reached , or any other kind of error occurs.
#  return 1 when action has been successfully been performed.
#  return 0 when action was deliberately not performed due to record already existing

#  S_No      Car_number       Timestamp of Entry     Gate of entry           status(bool)          Gate of exit

import mysql.connector as msq
from datetime import datetime as dt
import time

db = msq.connect(
    host="localhost",
    user="root",
    password="Karora@88",
    database = "carentryexit"
)

cur = db.cursor()

def check_status(car_number):
    try:
        command = f"select status from systum wher car_number = '{car_number}' ;"
        cur.execute(command)
        records = []
        for i in cur:
            records.append(i)
            if len(records)==0:
                return 0
            elif records[-1][0]==1:
                return 1
            else:
                return 0
    except:
        return -1
 

def enter(car_number, cur_time, entry_gate):
    status = check_status(car_number)
    if status == -1:
        return -1
    elif status == 1:
        return 0
    elif status ==0:
        try:
            command = f"insert into systum(car_number, timestamp_of_entry, status, Gate_of_entry) values ('{car_number}', '{cur_time}', '{entry_gate}');"
            cur.execute(command)
            db.commit()
            return 1
        except:
            return -1
        
def exit(car_number, cur_time, exit_gate):
    status = check_status(car_number)
    if status == -1:
        return -1
    elif status ==0:
        return 0
    elif status ==1:
        try:
            command = f"update systum set status=0, timestamp_of_exit , Gate_of_exit= '{cur_time}' where car number = '{car_number}' where exit_gate = '{exit_gate}'; "
            cur.execute(command)
            db.commit()
            return 1
        except:
            return -1
        

start = time.time()
enter("DL1CX2621", str(dt.now()),1)
end = time.time()
print(end-start)
exit("DL1CX2621", str(dt.now()),2)
