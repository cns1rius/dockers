#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import urllib3
import argparse
import time
import os

os.environ["NO_PROXY"] = "127.0.0.1"

urllib3.disable_warnings()

need = []


def sendMessage(msg, GROUP_NOTICE_ID, CQ_PORT=5700):
    try:
        request = requests.Session()
        url = f"http://127.0.0.1:{str(CQ_PORT)}/send_group_msg?group_id={str(GROUP_NOTICE_ID)}&message={str(msg)}"
        print(url)
        r = requests.get(url)
        # r = request.post(url, data=str(msg))
        print(
            "\033[32m[%s] [SEND] Sending message to %s\033[0m"
            % (
                str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))),
                GROUP_NOTICE_ID,
            )
        )
        print(r.json())
    except Exception as e:
        print(
            "\033[31m[%s] [ERROR] Error sending message to %s, Connection error possible port or address error\033[0m"
            % (
                str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))),
                GROUP_NOTICE_ID,
            )
        )
        print(e)


def get_events():
    url = "https://www.su-sanha.cn/api/events/list"
    events = requests.post(url).json()["data"]["result"]
    for event in events:
        if event["status"] == 1:
            need.append(event)

    choose_event()


def choose_event():
    file = open("./events.old")
    old_event = file.read()
    for event in need:
        if str(event["id"]) not in old_event:
            print(event["name"])
            msg = f"""比赛名称：{event["name"]}\n比赛链接：{event["link"]}\n比赛类型：{event["type"]}
报名开始：{event["bmks"]}\n报名截止：{event["bmjz"]}
比赛开始：{event["bsks"]}\n比赛结束：{event["bsjs"]}
其他说明：{event["readmore"]}"""
            sendMessage(msg, GROUP_NOTICE_ID, CQ_PORT=5700)

    sendMessage("请及时报名推送过的比赛", GROUP_NOTICE_ID, CQ_PORT=5700)
    file.close()
    file = open("./events.old", "w")
    for event in need:
        file.write(str(event["id"]) + "\n")
    file.close()


def main():
    global URL, GROUP_NOTICE_ID, MATCH_ID, CQ_PORT
    print("Pushing CTF events...")
    parser = argparse.ArgumentParser(description="CTF events push Bot")
    parser.add_argument("--notice", required=True, help="qq notice Group")
    parser.add_argument("--port", required=False, help="cq port")
    args = parser.parse_args()

    GROUP_NOTICE_ID = args.notice
    CQ_PORT = args.port

    get_events()


if __name__ == "__main__":
    main()