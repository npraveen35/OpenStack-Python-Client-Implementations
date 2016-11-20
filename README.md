# OpenStack-Python-Client-Implementations
Python code implementations using OpenStack Python clients - keystone, nova, neutron, glance

My Working Environment: On Ubuntu platform, created a virtualenv & installed openstack client. Then i built & executed these scripts to consume RESTful APIs. 

    sudo apt-get install python-pip -y
    sudo pip install --upgrade pip # my version is 9.0.1
    sudo pip install virtualenv # my version is 15.0.1
    virtualenv api_env
    cd api_env
    source bin/activate
    pip install python-keystoneclient

My OpenStack (Mitaka) environment is on CentOS 7 Server deployed by Packstack for which api calls were made.
