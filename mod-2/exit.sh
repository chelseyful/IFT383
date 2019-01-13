#!/bin/bash
LIST=`ls -l /doesnotexist 2> /dev/null`
echo "I ran ls and it said: ${?}"
