#!/bin/bash
read -p "Enter a list of colors, separated by a space: " -a COLORS
for COLOR in ${COLORS[*]}; do
	echo $COLOR
done
IFS=','
read -p "Enter a list of numbers, separated by a comma: " NUMBERS
for NUMBER in $NUMBERS; do
	echo $NUMBER
done
unset IFS
# C-style for loop
read -p "Enter a list of names separated by a space: " -a NAMES
for (( i=0; $i < ${#NAMES[*]}; i++ )); do
	echo -e "Input at position ${i} was ${NAMES[$i]}"
done
