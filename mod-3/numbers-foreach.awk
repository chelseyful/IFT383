BEGIN {
	FS=","
	OFS="\t"
	OFMT="%.2f"
	CSUM[0]=0;
	print "#1","#2","#3","#4","#5","SUM","AVG"
}
{
	RSUM=0
	for (i=1; i <= NF; i++) {
		CSUM[int(i)] += $i
		RSUM += $i
	}
	print $1,$2,$3,$4,$5,RSUM,RSUM/NF
}
END {
	print "---------------------------"
	for (NUMBER in CSUM) {
		if (NUMBER != 0) {
			print "Column " NUMBER " total is: " CSUM[NUMBER]
		}
	}
}
