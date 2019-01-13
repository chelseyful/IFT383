#!/bin/bash
declare -i SUM=0
declare -i INPUT=0
while (($INPUT > 0 || $SUM == 0)); do
	read -p "enter an integer, or nothing to stop: " INPUT
	SUM=$(( $SUM + $INPUT ))
done
echo -e "Your total is: ${SUM}"
SUM=0
INPUT=0
until (($SUM > 10)); do
	read -p "You have ${SUM} apples, how many apples to add? " INPUT
	SUM=$(($SUM + $INPUT))
done
echo -e "WOW! ${SUM} apples! that is too many apples!!"
