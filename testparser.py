#! /usr/bin/python3

import lib.getjson as getjson
import lib.servicehealthcheck as hcheck
import time

filelocation = "exam.json"      #location of JSON file
r = 6                           #number of trys
c = 10                          #interval in seconds between each try

def retrytillsuccess(reties, interval):
    def wrapper(fuc):
        n = 1
        while n <= reties:
            stat = fuc()
            if stat == "JSON is Healthy":
                print(stat)
                exit(1)
            print(stat + ' {n}/{c}'.format(n=n, c=reties))
            time.sleep(interval)
            n += 1
    return wrapper


@retrytillsuccess(r, c)
def cycle():
    datafile = getjson.loadjsonfile(filelocation)
    status = hcheck.checkhealth(datafile)
    return 'JSON is ' + status
