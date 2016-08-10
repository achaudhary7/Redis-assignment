
import json
import redis 
import ast
import sys
import argparse

__author__ = 'Anup Chaudhary'

def insert():
    readfile = open("input.json", "r")
    filedata = readfile.read()
    parsed_json = json.loads(filedata)
    lengthe = len(parsed_json)
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    key = 0
    while (key < lengthe):
        value =  parsed_json[key]
        hostid= value['hostIdentifier']
        column = value['columns']
        portno = column['port']
        sport =  repr(portno)
        r.sadd(hostid, portno)
        key = key + 1
    return hostid

def get_port(args):

    hostid = format(args.host)
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    portno = r.smembers(hostid)
    tolist = list(portno)
    portno = str(tolist)
    return portno



def main():

    parser = argparse.ArgumentParser(description='find port')
    parser.add_argument('-ht', '--host', type=str, help='Host name')
    args = parser.parse_args()

    inserall= insert()
    allport = get_port(args)

    print allport
if  __name__ =='__main__':main()


