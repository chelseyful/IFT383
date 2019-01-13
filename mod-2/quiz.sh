#!/bin/bash
# Conditional based on an integer
declare -l ANSWER=''
read -p "The author of the original version of grep was _______ Ritchie.: " ANSWER
if [ $ANSWER = 'dennis' ]; then
	echo "Correct!"
else
	echo "Sorry, try again"
fi
