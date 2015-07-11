#! /usr/bin/env python
import sys, os
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(MAIN_DIR, ".."))
#----------------------------------------------------------------------------------------------------------------------



from gcm import GCM
from general import config
import requests

GCM_URL = 'https://android.googleapis.com/gcm/send'

data = { "notification": {
    "title": "Portugal vs. Denmark",
    "text": "5 to 1"
  },
  "to" : "dcuSEmbXdtc:APA91bFwLCRoFhqPoKsk6hitWwqRH46TsyR7IRqaXQGG6zsziv6UEtckFFgw8umvD4K9G5ofPcIiBUn41ObWO1jpI_byhzN7a3rOtA1CcNdDdyvljWpZJyuB7oKQr5aDgzUGbpZ-sF5X"
}

headers = {
            'Authorization': 'key=%s' % config.GCM_KEY
        }

print(str(requests.post(
            GCM_URL, data=data, headers=headers
        )))