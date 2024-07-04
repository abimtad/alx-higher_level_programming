#!/bin/bash
# curl command to get the content size of the message body
curl -sl "$1" | wc -c
