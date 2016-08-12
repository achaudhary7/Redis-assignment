


#Sets
We have used this commands to create sets different of elements, To add a member to a set you have to use the SADD command, 
to remove a member we can use "SREM" command, to check if a member already exists the "SISMEMBER" command and to get the members of a set the "SMEMBERS" can be use.On Sets we can perform different operaions like UNION, Intersection ect.


So, Here if you run the above file you should get output like below-
```
1. To get the all ports associated with the host identifier-

$ find_hosts -ht='hostid'        
[ 'port1', 'port2', [], [], ]		  

2. To get the all hosts associated with the port no-

$ find_hosts -p=01
['host1', 'host2', 'host3..']		

3. To get the all hosts associated with the IP-

$ find_hosts -i=0.0.0.0
['host1', 'host2', 'host3..']		

4. To get the host associated with the port & IP-

$ find_hosts -p=5353 -i=0.0.0.0
['host1', 'host2', 'host3..']   
```





