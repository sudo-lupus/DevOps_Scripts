#!/usr/bin/env python3

import shutil
import psutil

def check_disc_usage(disk = "/", threshold = 0.2):
    du = shutil.disk_usage(disk)
    percentage_free = du.free / du.total * 100
    return percentage_free, percentage_free > threshold * 100

def check_cpu_usage(threshold = 75):
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage, cpu_usage < threshold

cpu_usage = check_cpu_usage()
disk_usage = check_disc_usage()

print(f"""Current Disk Usage:\t{round(100 - disk_usage[0], 2)}%
Current CPU Usage:\t{cpu_usage[0]}""")

if cpu_usage[1] == False or disk_usage[1] == False:
    print("ERROR!")
else:
    print("Everything is OK!")
