import requests
import json
import time

##Spark API call to send a message to the roomId.
def sparkCall(mymsg):
	url = "https://api.ciscospark.com/v1/messages"

	#payload = "{\n\t\"roomId\": \"Y2lzY29zcGFyazovL3VzL1JPT00vMjE0ODYwNTAtZjZkMC0xMWU1LThmOWYtYmQ5ZjQ4OTI3OGZh\",\n\t\"text\": \"Hi John\"\n}"
	payload  = {
		"roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vZWFjZDc2NjAtZmRlNS0xMWU1LWFjZGItYjlhMzIwZjE0NDAw",
		"text": mymsg
	}
	headers = {
	    'content-type': "application/json",
	    'authorization': "Bearer ODA0MjA1ZTMtZDBhNi00NTYzLWE4NjUtZmY0YTIxZTY2NWI3MzQ4YTRkMDYtN2Nm",
	    'cache-control': "no-cache",
	    'postman-token': "1a5747a0-8dff-d146-3724-c30bdfe5080e"
	    }


	response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

## showCommand function.  Takes a show command and returns the results
def showCommand(mycmd):
	url='http://198.18.134.17/ins'
	switchuser='admin'
	switchpassword='Cisco321'

	myheaders={'content-type':'application/json'}
	payload={
	  "ins_api": {
	    "version": "1.0",
	    "type": "cli_show",
	    "chunk": "0",
	    "sid": "1",
	    "input": mycmd,
	    "output_format": "json"
	  }
	}
	response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

	print (response)
	return response
## end def showCommand(mycmd): function

cmd = "show vlan"
while(1):
	response= showCommand(cmd)
	vlanData = response["ins_api"]["outputs"]["output"]["body"]["TABLE_vlanbrief"]["ROW_vlanbrief"]
	#print (vlanData)
	for vlanshowinfovlanid in vlanData:
		vlanNum = int(vlanshowinfovlanid["vlanshowbr-vlanid-utf"])
		vlanShutState = vlanshowinfovlanid["vlanshowbr-shutstate"]
		print ()
		print ("vlanNum: ",vlanNum)
		print ("vlanShutState: ", vlanShutState)	
		if (vlanNum == 45):
			if (vlanShutState == "shutdown"):
				print("OH NO, VLAN 45 is SHUTDOWN")
				sparkCall("OH NO, VLAN 45 is SHUTDOWN")
			if (vlanShutState == "noshutdown"):
				print("Yay, VLAN 45 is UP")
				sparkCall("Yay, VLAN 45 is UP")
	time.sleep(10)