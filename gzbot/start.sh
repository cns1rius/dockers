#!/bin/sh
###
 # @Author: s1rius
 # @Date: 2023-10-12 21:26:22
 # @LastEditTime: 2023-10-30 20:39:41
 # @Description: https://s1rius.space/
### 
sed -i "s/QQpasswd/$QQpasswd/g" ./gzbot/config.yml
mkdir gzbot/logs

echo qsign
systemctl start qsign
systemctl status qsign
sleep 3

cd gzbot

echo qqbot python
python3 gzbot.py --url="$1" --notice=$2 --id=$3 --port=5700 &

echo qq server
go-cqhttp > logs/server.log &
tail -f logs/server.log