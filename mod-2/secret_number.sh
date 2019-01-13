#!/bin/bash
declare -i NUMBER=0
read -p "Guess the secret number between 1 and 100: " NUMBER
if (( ($NUMBER + 30) / 2 == 36)); then
	echo -e "You got it!"
else
	echo -e "NOPE! try again"
fi

