
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
        r.sadd(portno, hostid)
        key = key + 1
    return hostid



def get_host(args):

    portno = format(args.port) #command line port no
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    hostname = r.smembers(portno)
    tolist = list(hostname)
    hostname = str(tolist)
    return hostname



def main():

    parser = argparse.ArgumentParser(description='Script retrieves schedules from a given server')
    parser.add_argument('-p', '--port', type=str, help='Port no')
    args = parser.parse_args()

    inserall= insert()
    allhost = get_host(args)

    print allhost

if  __name__ =='__main__':main()


