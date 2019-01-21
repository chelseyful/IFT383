# Use with buildings file
# counts number of single and multi-story buildings
BEGIN {
	MULTI=0
	SINGLE=0
	FS=","
	OFS="\t"
	OFMT="%.2f"
}
{
	if ($3 > 1) {
		MULTI++
	} else {
		SINGLE++
	}
	print $1,$2,$3
}
END {
	print "There are " SINGLE " single-story and " MULTI " multi-story buildings"
}
