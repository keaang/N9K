import requests
import json

def configInterface(cmd):
	url='http://198.18.134.17/ins'
	switchuser='admin'
	switchpassword='Cisco321'

	myheaders={'content-type':'application/json'}
	payload={
	  "ins_api": {
	    "version": "1.0",
	    "type": "cli_conf",
	    "chunk": "0",
	    "sid": "1",
	    "input": cmd,
	    "output_format": "json"
	  }
	}
	response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
	print (response)


for count in range(0,3):
	interface = "interface eth1/" + str(7+count)
	ipAddress = "192.168." + str(count) + ".1"
	subnetMask = "255.255.255.0"	
	cmd = "config term ;" + interface + " ;no switchport ;" + " ip address " + ipAddress + " " + subnetMask + " ;no shut"
	print ("cmd:", cmd)
	configInterface(cmd)

cmd = "config term ;vlan 45 ;no shut"
configInterface(cmd)
