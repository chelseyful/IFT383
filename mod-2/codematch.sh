#!/bin/bash
# Conditional based on an integer
declare -i PIN
read -p "Please enter your 4-digit PIN: " PIN
declare -i VALID=0
VALID=`echo -e "${PIN}" | grep -Ec "^[0-9]{4}$"`
if [ $VALID -eq '0' ]; then
	echo "You did not enter a valid code!"
elif [ $PIN -eq '1234' ]; then
	echo "Access Granted!"
else
	echo "Sorry, wrong code..."
fi
