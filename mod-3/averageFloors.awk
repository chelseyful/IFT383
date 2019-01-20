BEGIN {
	COUNT=0
	TOTAL=0
	FS=","
	OFS="\t"
}
$3~/[0-9]/ {
	COUNT++
	TOTAL+=$3
	print $1,$2,$3
}
END {
	print "Floor Stats:"
	print "Average",TOTAL/COUNT
}
