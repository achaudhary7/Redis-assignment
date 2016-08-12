
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
        sport = str(portno)
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
    portno = str(argsport) #command line port no
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
    argslen = len(sys.argv)

    if argslen == 2:
        if args.port:
            allhost = get_host(args.port)
            print allhost

        if args.host:
            allport = get_port(args.host)
            print allport

        if args.ip:
            allhost = get_ihost(args.ip)
            print allhost

    if args.port:
        if args.ip:
            alliphost = get_iphost(args)       
               
if  __name__ =='__main__':main()
