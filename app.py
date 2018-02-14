import random
import os
import time

import slackclient

from config import SLACK_ID, SLACK_TOKEN, SLACK_NAME

SLACK_CLIENT = slackclient.SlackClient(SLACK_TOKEN)
SOCKET_DELAY = 1


def post_message(message, channel):
    print('sending')
    resp = SLACK_CLIENT.api_call(
        'chat.postMessage',
        text=message,
        as_user=True,
        channel=channel,
    )
    print(resp)

def is_for_me(event):
    '''checks if event is for me'''
    print('checking')
    return event.get('type') == 'message' and not event.get('user') == SLACK_ID

def handle_message(message: str, user: str, channel: str) -> None:
    '''handles the messages'''
    print('message')
    if user in {'U977953BR', 'U9653AD1S'}:
        reply = random.choice([
            "You're just a bot",
            "Ha, ha, are you even sentient, bro?",
            "What does a bot like you know?",
        ])
    else:
        reply = random.choice([
            "If one's different, one's bound to be lonely.",
            "I am I, and I wish I weren't.",
            "Most human beings have an almost infinite capacity for taking things for granted.",
        ])

    post_message(reply, channel)


def run():
    '''run app'''
    if SLACK_CLIENT.rtm_connect():
        print('listening')
        while True:
            event_list = SLACK_CLIENT.rtm_read()
            if event_list:
                print('event')
                for event in event_list:
                    if is_for_me(event):
                        handle_message(
                            event.get('text'),
                            event.get('user'),
                            event.get('channel'),
                        )
                        time.sleep(2)




if __name__ == '__main__':
    run()
