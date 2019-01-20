BEGIN {
	FS=","
	RS=";"
	OFS="\t"
	ORS="\n"
	print "#","Short","Full Name"
}
$1~/[0-9]/ {
	print $1,$2,$3
}
END {}
