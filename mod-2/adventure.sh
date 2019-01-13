#!/bin/bash
declare -u CHOICE1=''
read -p "You are standing in front of a house, surrounded by an old wooden fence. You can move North, East, South or West. In what direction do you travel? " CHOICE1
case $CHOICE1 in
	N|NORTH)
		echo -e "You move towards the house, and notice an old, sleeping dog on the porch"
		;;
	E|EAST)
		echo -e "You walk towards the side of the house and notice something on the ground..."
		;;
	S|SOUTH)
		echo -e "You move away from the house and begin walking down a dimly lit street"
		;;
	W|WEST)
		echo -e "You are eaten by a grew. Game over."
		;;
	* )
		echo -e "Invalid selection, please try again"
		;;
esac
