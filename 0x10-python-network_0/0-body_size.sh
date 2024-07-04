#!/bin/bash
# curl command to get the content size of the message body
curl -sI "$1" | grep -i content-length | wc -c
