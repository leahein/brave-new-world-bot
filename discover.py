import slackclient

from config import SLACK_TOKEN, SLACK_NAME

SLACK_CLIENT = slackclient.SlackClient(SLACK_TOKEN)
is_ok = SLACK_CLIENT.api_call('users.list').get('ok')

if is_ok:
    for user in SLACK_CLIENT.api_call('users.list').get('members'):
        if user.get('name') == SLACK_NAME:
            slack_app_id = user.get('id')
            print(slack_app_id)
