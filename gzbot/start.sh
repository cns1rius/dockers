#!/bin/sh
sed -i "s/QQpasswd/$QQpasswd/g" ./gzbot/config.yml
mkdir gzbot/logs

echo qsign
java -jar unidbg-fetch-qsign-all.jar --basePath=./txlib/8.9.73 > gzbot/logs/qsign.log &
sleep 3

cd gzbot

echo qqbot python
python3 gzbot.py --url="http://10.101.162.163" --notice=$1 --id=$2 --port=5700 &

echo qq server
go-cqhttp