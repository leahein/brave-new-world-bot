import os

import yaml

PATH_ROOT = os.path.dirname(os.path.realpath(__file__))
PATH_CRED = os.path.join(PATH_ROOT, 'credentials.yaml')

with open(PATH_CRED, 'r') as creds:
    CREDENTIALS = yaml.load(creds.read())


SLACK = CREDENTIALS['slack']
SLACK_TOKEN = SLACK['api_token']
SLACK_NAME = SLACK['name']
SLACK_ID = SLACK['api_id']
