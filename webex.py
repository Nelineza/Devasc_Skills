import requests
import json

access_token = "NjVjMzQ0MjEtNjNjNC00ZDY3LTljMzktMzk0MjliODMwMjk2MGE3ZWE4MTUtOWMz_PE93_74cc8408-7643-4e09-b2b1-682def4bf071"

groups_struc = {
 "groups": [
      { "group": { "group_id": "G1" , "group_name": "GROUP_YRO_A" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "Nick", "email": "nick@biasc.be"},
                     {"person_id": "P-2" , "person_name": "Marcus", "email": "marcus@biasc.be"},
                     {"person_id": "P-3" , "person_name": "Lisa", "email": "lisa@biasc.be"} 
                   ]
                 }
      }
 ]
}

url = 'https://webexapis.com/v1/rooms'
headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }
for rec in groups_struc["groups"]:
    create_group_name = rec["group"]["devasc_skills_NIN"]
    print("Creating ... " + create_group_name)
    payload_space={"title": create_group_name}
    if payload_space["title"] != None:  ### avoid errors if room title is unknown
        res_space = requests.post(url, headers=headers, json=payload_space)
        if res_space.status_code < 300: ### only create members if space has been created
            NEW_SPACE_ID = res_space.json()["id"]
            for mbr in rec["group"]["members"]:
                room_id = NEW_SPACE_ID
                person_email = mbr["yvan.rooseleer@biasc.be"] 
                url2 = 'https://api.ciscospark.com/v1/memberships'
                payload_member = {'roomId': room_id, 'personEmail': person_email}
                res_member = requests.post(url2, headers=headers, json=payload_member)

