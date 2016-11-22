# This script is an example usage of python-keystoneclient
# Author: Praveen N

from keystoneclient.v2_0 import client as ksclient
from config import USER,PWD,TENANT,AUTH_URL, print_table

try:
    keystone = ksclient.Client( username=USER, password= PWD, tenant_name=TENANT, auth_url= AUTH_URL)
    
    tenants = keystone.tenants.list() # list of class objects
    print '+' * 65
    print "\n *** Tenants List ***\n"
    print_table('ID','Name', tenants)
     
    services = keystone.services.list()
    print "\n *** Services List ***\n"
    print_table('ID','Name', services)

    users = keystone.users.list()
    print "\n *** Users List ***\n"
    print_table('UUID', 'Tenant Name', users)

    roles = keystone.roles.list()
    print "\n *** Roles List ***\n"
    print_table('ID','Roles', roles)

except:
    print "Invalid Access !!"
    
    '''     
    tenants = keystone.tenants.list() # list of class objects
    print '+' * 65
    print "\n *** Tenants List ***\n"
    tenants_table = PrettyTable(['UUID', 'Tenant Name'])
    for t in tenants:
        tenants_table.add_row([t.id, t.name])
    print tenants_table
    print '+' * 65
    
    users = keystone.users.list() 
    print "\n *** Users List ***\n"
    users_table = PrettyTable(['UUID', 'Name'])
    for u in users:
        users_table.add_row([u.id, u.name])
    print users_table
     
    roles = keystone.roles.list()
    print '+' * 65
    print "\n *** Roles List ***\n"
    roles_table = PrettyTable(['ID','Roles'])
    for r in roles:
        roles_table.add_row([r.id, r.name])
    print roles_table
        
    services = keystone.services.list()
    print '+' * 65
    print "\n *** Services List ***\n"
    service_table = PrettyTable(['ID','Name','Type'])
    for s in services:
        service_table.add_row([s.id, s.name, s.type ])
    print service_table
    print '+' * 65
    '''

