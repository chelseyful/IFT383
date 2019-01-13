#/bin/bash
read -p "Please enter the cost of three items on your bill, separated by spaces: " -a BILL
SUBTOTAL=`echo "scale=2; ${BILL[0]} + ${BILL[1]} + ${BILL[2]}" | bc`
DUE=`echo "scale=2; ($SUBTOTAL*0.15)+$SUBTOTAL" | bc`
echo "You entered: ${BILL[*]}"
echo "Your total bill, including 15% tip is; ${DUE}"
