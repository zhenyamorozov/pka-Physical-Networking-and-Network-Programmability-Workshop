## What this is
This is a workshop that demonstrates how very different concepts - physical networking and network programmability - may be brought together to create an interactive, fun and educational experience.
From learner's perspective, the task is to fix patch cabling in an office LAN, but their progress is tracked and posted to a Webex space. As an optional step, it is possible to review the code. 

Recording of the webinar with workshop presentation: https://netacad.webex.com/netacad/lsr.php?RCID=0a4164671ce875b0fc54d14be96a70bc

## Files
- `Physical Networking and Network Programmability Workshop.pka` - the Packet Tracer Activity file. [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer) is required to open it.
- `*.png` - image files that go along with the PKA
- `code.py` - the python code that is also enclosed in the PKA (PC-A - Programming tab)

## How to replicate

Here are the steps to make this activity work with your own Webex bot in your own Webex room:
1.	Create your own bot:
	- Go to http://developer.webex.com and Log in 
    - Click your profile picture in the top right and select My Webex Apps
    - Create a New App
	- Create a Bot
	- Input bot name, unique username, icon and description
	- Copy and save somewhere the **Bot access token**
2.	Create a new Webex room:
	- In your Webex client, click + , then Create a space, or similar
	- Add you bot to the room using the Bot username (email address)
3.	Copy the new room ID:
	- Go to the API Documentation here: https://developer.webex.com/docs/api/v1/rooms/list-rooms
	- The API documentation let you run calls right there. Make sure the Try it mode is on.
	- Scroll down and click Run button.
	- In the JSON response, identify the new room (it will likely be the first one) and copy the value if the “id” field. This is your **room ID**.
4.	Open the PKA and modify:
	- Perform a few first steps of the lab: add a switch, connect PC-A and PT-Controller0 to the switch
	- Click PC-A, then Programming tab
	- Replace in the postToWebex() function:
	    - accessToken with your **bot access token**.
	    - roomId with your **room ID**.
	- Stop the code and Run again.
	- Observe the output in the console below. If you see status code 200, it works. Otherwise, error messages should help you troubleshoot.
5.	**IMPORTANT:** To make your code changes permanent, you must make them to the Initial topology in the Activity Wizard. Otherwise Reset Activity action will erase your modifications. To do that:
	- Click Extensions – Activity Wizard
	- Enter the activity password. This activity uses the same password as all CCNA7 activities. This password may be found in NetAcad Communities – Packet Tracer Community.
	- In Activity Wizard, click Initial Network, Show Initial Network.
	- Navigate to Physical workspace, wiring closet, click PC-A and make the code changes listed above.
	- Back in Activity Wizard, Save your activity as PKA. 
6. You are done.
