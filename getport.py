
import json
import redis 
import ast


def main():
	try:
		readfile = open("input.json", "r")
		filedata = readfile.read()
		parsed_json = json.loads(filedata)
		lengthe = len(parsed_json)
	except (ValueError, KeyError, TypeError):
		print "ERROR In Parsing JSON"

	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	key = 0
	while (key < lengthe):
		value =  parsed_json[key]
		r.hmset(key, value)         #store list into redis 
		getall = r.hgetall(key)
		hostid= getall['hostIdentifier']  #get all host id
		getcolumn = getall['columns'] 
		getcolumndata = ast.literal_eval(getcolumn) # Convert into directory 
		portno = getcolumndata['port']  #extract the portnos
		r.sadd(hostid, portno)         #add it into redis db
		portno = r.smembers(hostid)   #get port no for all host
		sport =  str(portno)          #conver set into string
		print "For Host ID: " + hostid + ", " "Port Nos is: " + sport
		key = key + 1
if __name__ == '__main__':
	main()





# #r.sadd(hostid, portno)
# portno = r.smembers("host14")
# portno.remove("#657")
# print portno


# key = 0
# while (key < lengthe):
# 	value =  parsed_json[key]
# 	r.hmset(key, value)
# 	getall = r.hgetall(key)
# 	#print getall
# 	hostid= getall['hostIdentifier']
# 	#print hostid
# 	getcolumn = getall['columns'] 
# 	getcolumndata = ast.literal_eval(getcolumn) # Convert into directory 
# 	portno = getcolumndata['port']
# 	sport =  repr(portno)
# 	r.sadd(sport, hostid)
# 	#print portno
# 	key = key + 1

# portno = r.smembers(sport)
# print portno
	







	
	
	