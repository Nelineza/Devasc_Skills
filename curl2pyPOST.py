import requests

headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
}

data = '{\n       "severity": "alerts"\n}'

response = requests.post('https://192.168.56.107:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor', headers=headers, data=data, verify=False, auth=('cisco', 'cisco123!'))