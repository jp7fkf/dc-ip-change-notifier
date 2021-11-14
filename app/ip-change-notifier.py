#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author: Yudai Hashimoto
# https://jp7fkf.dev/

import os
import requests
import json
import traceback
import urllib.request

SLACK_URL = os.environ['SLACK_URL']
IPINFO_URL = 'https://ipinfo.io'
IPFILE_PATH = 'ipaddress.txt'

def send_slack(slack_text):
  payload = {
    "username": "IP Address Change Notifier",
    "icon_emoji": ':rotating_light:',
    "attachments": [{
    "text": slack_text,
    "color": "#ff0000",
    }
  ]}

  data = json.dumps(payload)
  requests.post(SLACK_URL, data)

def main():
  previous_ipaddr = ''

  try:
    response = urllib.request.urlopen(IPINFO_URL)
  except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
  except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)

  data = json.loads(response.read())
  current_ipaddr = data["ip"]

  try:
    f = open(IPFILE_PATH, mode='r')
    try:
      previous_ipaddr = f.read()
    except:
      print(traceback.format_exc())
    finally:
      f.close()
  except IOError:
    previous_ipaddr = ''

  # if some diff of addrs exists:
  if (current_ipaddr != previous_ipaddr):
    try:
      f = open(IPFILE_PATH, mode='w')
      try:
        f.write(current_ipaddr)
      except:
        print(traceback.format_exc())
      finally:
        f.close()
    except:
      print(traceback.format_exc())

    data_str = json.dumps(data, indent=2)
    slack_text = f'IP Address Changed! : {current_ipaddr} ```{data_str}```'
    send_slack(slack_text)

if __name__ == "__main__":
  try:
    main()
  except:
    slack_text = f'Exception occurred!'
    send_slack(slack_text)
