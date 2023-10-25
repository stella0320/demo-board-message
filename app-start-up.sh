#!/bin/bash
# time: 2023/10/19

# Author: Jessie Chen

echo -e "start"

nohup python3 /app/demo-board-message/app.py &

exit 0

echo $?
