#!/usr/bin/python

# Yiming Shao@
# A program to record how long the user worked/studied
# Input
import os
from datetime import datetime, timedelta

def main():
    print ("Do not change your local txt file \n \n")
    my_path = 'threedays_program.txt'
    my_file = open(my_path, "a+")
    key = rec_input()

    if not check_Empty(my_path):
        if key != "start":
            print("You should start first")
            key = rec_input()
        else:
            my_file.write("start: " + str(record_current_date())+"\n")

    if check_Empty(my_path):
        my_file = open(my_path)
        lines = my_file.readlines()
        lastline = lines[len(lines)-1]
        if "start" in lastline and key=="start":
            print("You are studying")
            return
        if "stop" in lastline and key=="stop":
            print("You need to start first")
            key = rec_input()
        else:
            my_file = open(my_path,"a+")
            if key=="start":
                my_file.write("start: " + str(record_current_date()) + "\n")
            if key== "stop":
                date_str = 'start: %Y-%m-%d %H:%M:%S\n'
                starting_time = datetime.strptime(lastline, date_str)
                ending_time = record_current_date()
                time_diff = ending_time-starting_time
                my_file = open(my_path, "a+")
                my_file.write("stop: " + str(ending_time)+"\n")
                print("You studied "+str(time_diff))


def check_Empty(path):
    if os.path.getsize(path)>0:
        return True
    else:
        return False

def rec_input():
    key = input("Enter your status: ");
    if key != "start" and key != "stop":
        print("You should enter 'start' or 'stop' ")
        return rec_input()
    return key



def record_current_date():
    clock = datetime.now()
    return (datetime(clock.year,clock.month,clock.day,clock.hour,clock.minute,0))


if __name__ == '__main__':
    main()
