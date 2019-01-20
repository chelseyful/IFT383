BEGIN {
	split("Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec",MONTHS,",")
	FS=","
	OFS="\t"
}
{
	print $2,MONTHS[int($1)],$3
}
END {}
