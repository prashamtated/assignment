#!/usr/bin/env python3

'''
Author - Prasham Tated

Solving Problem statement -
Attached you will find a JSON file (meta.json) that contains an array of objects each of which has a "creationTimestamp" field.
i).  Create a script which takes two inputs, number of days and match pattern
ii). After giving input the script should display the count of objects that will match below conditions.
	Objects created before a number of days provided.
	Objects that only match the pattern.

'''

import json
import datetime
import sys

#'''
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print ('''This script require 2 argument to process 
        1. number of days 
        2. pattern to match in json object 
        ''')
        sys.exit(1)
#    for i, arg in enumerate(sys.argv):
#        print(f"Argument {i:>3}: {arg}")
#'''

with open('metadata.json') as f:
    data = json.load(f)
    #print(len(data))

numDays = int(sys.argv[1])
pattern = sys.argv[2]

#print (pattern, numDays)


def checkdate(numDays, timestamp):
    b0 = timestamp
    b1 = datetime.datetime.strptime(b0, '%Y-%m-%dT%H:%M:%S')
    #print(b1)
    b2 = datetime.datetime.now() - datetime.timedelta(days=numDays)
    #print(b2)
    # Check the dates
    if b1 == b2:
        #print("Both persons are of equal age")
        return False
    elif b1 > b2:
        #print("The second person is older")
        return False
    else:
        #print("The first person is older")
        return True


counter = 1

for p in data:
    #print('Name: ' + p['name'])
    if checkdate(numDays, p['creationTimestamp'][0:19]):
        if pattern in p['name']:
#            print("yes", counter)
            counter = counter + 1


    #print('')
print('')
print(f"Number of object found by matching pattern:'{pattern}' in Object name and data created '{numDays}' days before are:'{counter - 1}'")
print('')