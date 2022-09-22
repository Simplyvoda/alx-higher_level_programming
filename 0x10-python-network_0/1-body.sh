#!/bin/bash
# this script takes in a URL sends a GET req. to the URL and displays response body
curl -sfL "$1" -X GET
