
import json
import redis 
import ast
import sys
import argparse
r = redis.Redis(host='localhost', port=6379) #Initilize redis db
            
                                                        #This will return port no associated wil host id
def get_port(argshost):
    hostid = format(argshost)
    portno = r.smembers(hostid)
    portno = list(portno)
    return portno

#This will return host no associated wil port id
def get_host(argsport):
    portno = str(argsport) #command line port no
    hostname = r.smembers(portno)
    tolisthostname = list(hostname)
    return tolisthostname


#This will return host no associated wil Ip address
def get_ihost(argsip): 
    ip =  str(argsip)
    sip = format(ip)
    hostname = r.smembers(argsip)
    tolisthostname = list(hostname)
    return tolisthostname


#This will return host no associated wil port id & ip address
def get_iphost(args):
    portno = format(args.port)
    ip = format(args.ip)
    hostname = r.sinter(portno, ip)  #Perform intersection 
    tolisthostname = list(hostname)
    return tolisthostname






def main():

    ## All command line arguments are define here
    parser = argparse.ArgumentParser(description='Script retrieves schedules from a given server')
    parser.add_argument('-ht', '--host', type=str, help='Host name')
    parser.add_argument('-p', '--port', type=str, help='Port number')
    parser.add_argument('-i', '--ip', type=str, help='IP address')


    inserall= insert()       # Call to insert function 

    args =  parser.parse_args()
    argslen = len(sys.argv)

    if argslen == 2:
        
        if args.port:
            allhost = get_host(args.port) 
            if allhost:
                print allhost              # print all host id associated with port

        if args.host:
            allport = get_port(args.host)
            if allport:
                print allport       # print all port no associated with host

        if args.ip:
            allhost = get_ihost(args.ip) 
            if allhost:
                print allhost          # print all host id associated with host

    if args.port:
        if args.ip:
            alliphost = get_iphost(args)
            if alliphost:
                print alliphost         # print all host id associated with ip & port



def insert():                               #This is the mail inser function 
    readfile = open("input.json", "r")
    filedata = readfile.read()
    parsed_json = json.loads(filedata)
    lengthe = len(parsed_json)
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

               
if  __name__ =='__main__':main()
