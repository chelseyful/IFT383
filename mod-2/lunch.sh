#!/bin/bash
declare -l LUNCH=''
declare -i STEP=1
function makeLunch {
	case $STEP in
		2) echo "Adding turkey meat...";;
		3) echo "Adding more bread...";;
		4) echo 'done';;
		*) echo "Adding bread...";;
	esac
}

until [ "${LUNCH}" = "done" ]; do
	LUNCH=$(makeLunch)
	echo -e "Preparing lunch: ${LUNCH}"
	((STEP++))
	sleep 1
done
