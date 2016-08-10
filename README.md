# Run File as below- 

$ find_hosts -ht='hostid'

[ 'port1', 'port2', [], [], ]		//Thsese all port associated with host          

$ find_hosts -p=01

['host1', 'host2', 'host3..']		//these all host associated with port


$ find_hosts -i=0.0.0.0

['host1', 'host2', 'host3..']		//these all host associated with ip

$ find_hosts -i=0.0.0.0 -p=01

['host1', 'host2', 'host3..']    //these all host associated with ip & port






