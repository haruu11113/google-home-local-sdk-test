import os
import json
import requests
from slack_sdk import WebClient
from dotenv import load_dotenv
import pandas as pd
load_dotenv(".env")

CHANNEL_ID = 'CAUTV3YRF'

def getHistory():
    client = WebClient(os.environ['SLACK_USER_TOKEN'])
    response = client.conversations_history(channel=CHANNEL_ID)
    messages = response.get('messages')
    return messages


def sentMessage(text="aaaaaaaa"):
    WEB_HOOK_URL = "{0}{1}".format(os.environ['SLACK_ROOT'], os.environ['SLACK_PATH'])
    requests.post(WEB_HOOK_URL, data = json.dumps({
        'text': '{0}'.format(text),
        'username': u'ubuntu server bot',
        'icon_emoji': u':smile_cat:',
        'link_names': 1,
    }))

messages = getHistory()
messages_df = pd.DataFrame(messages)
print(messages_df["text"].head())
