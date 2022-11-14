##What this is

##How to replicate

Here are the steps to make this activity work with your own Webex bot in your own Webex room:
1. Go to http://developer.webex.com and Log in 
2.	Create your own bot:
    - Click your profile picture in the top right and select My Webex Apps
    - Create a New App
	- Create a Bot
	- Input bot name, unique username, icon and description
	- Copy and save somewhere the **Bot access token**
3.	Create a new Webex room:
	- In your Webex client, click + , then Create a space, or similar
	- Add you bot to the room using the Bot username (email address)
4.	Copy the new room ID:
	- Go to the API Documentation here: https://developer.webex.com/docs/api/v1/rooms/list-rooms
	- The API documentation let you run calls right there. Make sure the Try it mode is on.
	- Scroll down and click Run button.
	- In the JSON response, identify the new room (it will likely be the first one) and copy the value if the “id” field. This is your **room ID**.
5.	Open the PKA and modify:
	- Perform a few first steps of the lab: add a switch, connect PC-A and PT-Controller0 to the switch
	- Click PC-A, then Programming tab
	- Replace in the postToWebex() function:
	    - accessToken with your **bot access token**.
	    - roomId with your **room ID**.
	- Stop the code and Run again.
	- Observe the output in the console below. If you see status code 200, it works. Otherwise, error messages should help you troubleshoot.
6.	**IMPORTANT:** To make your code changes permanent, you must make them to the Initial topology in the Activity Wizard. Otherwise Reset Activity action will erase your modifications. To do that:
	- Click Extensions – Activity Wizard
	- Enter the activity password. This activity uses the same password as all CCNA7 activities. This password may be found in NetAcad Communities – Packet Tracer Community.
	- In Activity Wizard, click Initial Network, Show Initial Network.
	- Navigate to Physical workspace, wiring closet, click PC-A and make the code changes listed above.
	- Back in Activity Wizard, Save your activity as PKA. 
7. You are done.
