
import json
import redis 
import ast
import sys
import argparse

## All command line arguments are define here
parser = argparse.ArgumentParser(description='Script retrieves schedules from a given server')
parser.add_argument('-ht', '--host', type=str, help='Host name')
parser.add_argument('-p', '--port', type=str, help='Port number')
parser.add_argument('-i', '--ip', type=str, help='IP address')

__author__ = 'Anup Chaudhary'


def insert():                               #This is the mail inser function 
    readfile = open("input.json", "r")
    filedata = readfile.read()
    parsed_json = json.loads(filedata)
    lengthe = len(parsed_json)
    r = redis.Redis(host='localhost', port=6379)
    key = 0
    while (key < lengthe):
        value =  parsed_json[key]
        hostid= value['hostIdentifier']
        column = value['columns']
        portno = column['port']
        ip = column['address']
        sip = str(ip)
        fip = format(ip)
        sport = repr(portno)
        r.sadd(sport, hostid)
        r.sadd(fip, hostid)
        r.sadd(hostid, portno)
        key = key + 1
    return hostid

#This will return port no associated wil host id
def get_port(argshost):
    r = redis.Redis(host='localhost', port=6379)
    hostid = format(argshost)
    portno = r.smembers(hostid)
    tolist = list(portno)
    portno = str(tolist)
    return portno

#This will return host no associated wil port id
def get_host(argsport):
    r = redis.Redis(host='localhost', port=6379)
    portno = format(argsport) #command line port no
    hostname = r.smembers(portno)
    tolist = list(hostname)
    hostname = str(tolist)
    return hostname

#This will return host no associated wil port id & ip address
def get_iphost(args):
    r = redis.Redis(host='localhost', port=6379)
    portno = format(args.port)
    ip = format(args.ip)
    hostname = r.sinter(portno, ip)
    tolist = list(hostname)
    hostname = str(tolist)
    return hostname

#This will return host no associated wil Ip address
def get_ihost(argsip):
    r = redis.Redis(host='localhost')    
    ip =  str(argsip)
    sip = format(ip)
    hostname = r.smembers(argsip)
    tolist = list(hostname)
    hostname = str(tolist)
    return hostname




def main():

    inserall= insert()
    
    args =  parser.parse_args()
    argshost =  str(args.host)
    argsip =  str(args.ip)
    argsport = str(args.port)
    print args
    if argshost == 'None':                    ## Get all host no associated with given port
        if argsip == 'None':
            allhost = get_host(argsport)
            print allhost

    if argsip != 'None':
        if argsport != 'None':
            alliphost = get_iphost(args)        ## Get all host no associated with given port & ip
            print alliphost
    
    if argshost != 'None':
        allport = get_port(argshost)            ## Get all port no associated with given host
        print allport

    if argshost == 'None':
        if argsport == 'None':
            allhost = get_ihost(argsip)            ## Get all port no associated with given host
            print allhost
               

if  __name__ =='__main__':main()


