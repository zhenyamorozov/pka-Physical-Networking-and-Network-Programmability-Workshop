"""
This script is intended to run in Cisco Packet Tracer environment
"""

import requests
import json
from time import *
import realhttp
import workspace



def getHostCount():
	baseUri = "http://192.168.1.254/api/v1"

	# API call to request service ticket
	headers = {"Content-Type": "application/json"}
	data = json.dumps( {"username": "cisco", "password": "cisco"} )
	
	try:
		resp = requests.post(baseUri+"/ticket", data=data, headers=headers)
	
		# print (resp.status_code)
		result = resp.json()
		# print (result)
		
		ticket = result["response"]["serviceTicket"]
		# print("Service Ticket: "+ticket)
	except:
		return 0
	
	# API call to request list of network devices
	headers = {"X-Auth-Token": ticket}
	try:
		resp = requests.get(baseUri+"/host", headers=headers)
		
		# print (resp.status_code)
		result = resp.json()
		# print (json.dumps(result, indent=4))
		
		count = 0
		for i in result["response"]:
			if i["pingStatus"]=="SUCCESS":
				count += 1
			
		return count
	except:
		return 0
	

def postToWebex(markdown):
	baseUri = "https://webexapis.com/v1/"
	accessToken = "replace-with-your-access-token"
	roomId = "replace-with-your-room-ID"
	
	
	def onHTTPDone(status, data, replyHeader): 
		print(status)
		# print(data)

	http = realhttp.RealHTTPClient()
	http.onDone(onHTTPDone)

	http.postWithHeader(
		baseUri+"messages",
		{"roomId":roomId, "markdown":markdown},
		{"Authorization":"Bearer "+accessToken, "Content-Type":"application/json"}
		)
		
	delay(5000)	



def main():

	hostCount = 0
	
	while True:
		lo = workspace.getLogicalObject()
		name = lo.getName()
		
		newHostCount = getHostCount()
		
		print ("%s - %d"%(name,newHostCount))
		
		if newHostCount != hostCount:
	
			text = "Host count for **%s** is now **%d**"%(name, newHostCount)
			if newHostCount==3 and newHostCount>hostCount:
				text += ". That's a good start!"
			if newHostCount==6 and newHostCount>hostCount:
				text += ". Way to go!"
			if newHostCount==10 and newHostCount>hostCount:
				text += ". Almost done!"
			if newHostCount==12 and newHostCount>hostCount:
				text += ". Activity complete, \n# Congratulations, %s!!"%name
	
			postToWebex(text)
			hostCount = newHostCount		

		delay(5000)


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    