#!/bin/awk
BEGIN {
	FS=","
	print "Code\tName\t\tFloors"
}
/./ {
	printf "%s\t%s\t\t%d\n",$1,$2,$3
}
END {
	print "All Done!\n"
}
