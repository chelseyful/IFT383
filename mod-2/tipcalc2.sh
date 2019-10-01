#!/bin/bash
read -p "Please enter the total on your bill: " BILL
TOTAL=`echo "scale=2; ($BILL*0.15)+$BILL" | bc`
echo "Your total bill, including 15% tip is; ${TOTAL}"
