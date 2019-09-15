#-*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import re
from slackclient import SlackClient


slack_client = SlackClient('your_token')
starterbot_id = 'your_bot_id'

RTM_READ_DELAY = 1 
EXAMPLE_COMMAND = "점심메뉴"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    matches = re.search(MENTION_REGEX, message_text)
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    default_response = "잘 모르겠어요. 이렇게 말해보세요 : *{}*.".format(EXAMPLE_COMMAND)
    response = None
    if command.startswith(EXAMPLE_COMMAND):
        response = "오늘 점심은 없다!"
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("커맨드봇이 연결되어 동작하고 있습니다.")
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("연결에 실패했습니다.")
