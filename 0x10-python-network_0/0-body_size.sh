#!/bin/bash
# print the length of file resource body
curl -sI "$1" | grep Content-Length | awk -F' ' '{print $2}'
