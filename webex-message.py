import requests
import os
 
# run code by running:
 
# export WBX_KEY="put key here"
# export WBX_ROOM_ID="put room id here"
# python send-msg.py
 
# The Message we send - roomname not needed, we get roomid from env vars below
 
TheMessage = "Here are my screenshots of devasc skills-based exam"
 
# setup vars - we get api key and roomid from environment variables
 
WEBEX_API="https://api.ciscospark.com/v1/"    # WEBEX_API="https://webexapis.com/v1/"
WBX_KEY = os.environ.get('WBX_KEY', '')
WBX_ROOM_ID = os.environ.get('WBX_ROOM_ID', '')
 
# setup session
 
webex_session = requests.Session()
webex_headers={"Authorization": "Bearer " + WBX_KEY}
webex_session.headers.update(webex_headers)
print(f"* {WEBEX_API=} {WEBEX_ROOMNAME=} {WBX_ROOM_ID=} {webex_headers=}")
 
# send message
 
webex_message_json = {
         "roomId": WBX_ROOM_ID,
         "text": TheMessage
        }
webex_message = webex_session.post(url=WEBEX_API+"messages",json=webex_message_json)
print(f"* {webex_message=}")
print(f"* {webex_message.json()=}")