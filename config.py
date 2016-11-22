#!/usr/bin/python
# AUthor: Praveen N
from prettytable import PrettyTable
 
#Username
USER = 'admin'

#Password
PWD = 'praveen'

#Tenant Name
TENANT = 'admin'

#Your OpenStack Server IP
IP = '172.27.3.90'

#Don't edit the below
AUTH_URL = str('http://'+ IP + ':5000/v2.0')


def print_table(*argv):
    my_table = PrettyTable([argv[0], argv[1]]) # columns in  pretty table 
    for t in argv[2]: # list of class objects are in argv[2]
        my_table.add_row([t.id, t.name])
    print my_table
    print '+' * 65
