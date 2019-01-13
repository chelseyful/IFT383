#/bin/bash
TOTAL=`echo "scale=2; ($1*0.15)+$1" | bc`
echo "Your total bill, including 15% tip is; ${TOTAL}"
