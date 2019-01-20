function printSep () {
	print "-----------------------------"
}
BEGIN {
	FS=","
	OFS="\t"
	OFMT="%.2f"
	CSUM[0]=0;
	print "#1","#2","#3","#4","#5","SUM","AVG"
	printSep()
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
	printSep()
	print CSUM[1],CSUM[2],CSUM[3],CSUM[4],CSUM[5]
}
