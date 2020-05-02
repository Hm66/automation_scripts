#! /usr/bin/env python3
import os
import requests
import json


dir_list = os.listdir("/data/feedback")
dictreq= {}
url = 'http://104.197.232.194/feedback/'
for file in dir_list :
    abs_file_path = os.path.join("/data/feedback/",file)
    print(abs_file_path)
    with open(abs_file_path) as p:
        lines = [line.rstrip('\n') for line in p]
        keys=['title', 'name', 'date', 'feedback']
        dictreq = dict(zip(keys,lines))
        print(dictreq)
        dataf = json.dumps(dictreq)
        headers = {'Content-type': 'application/json'}
        res = requests.post(url,data =test,headers=headers)
        if not response.ok:
            raise Exception("GET failed with status code {}".format(response.status_code))
        else:
            print(res.status_code)
