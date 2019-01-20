BEGIN {
	FS=","
	OFS="\t"
	print "#1","#2","#3","#4","#5","MIN","MAX"
}
{
	MIN=-1
	MAX=-1
	COL=1
	while (COL <= NF) {
		if ($COL < MIN || MIN == -1) {
			MIN=$COL
		}
		if ($COL > MAX || MAX == -1) {
			MAX=$COL
		}
		COL++
	}
	print $1,$2,$3,$4,$5,MIN,MAX
}
END {}
