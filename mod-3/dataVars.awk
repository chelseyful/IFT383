# Use with buildings file
BEGIN {
	FS=","
	OFS="\t"
}
{
	print NR,$1,$2,$3
}
END {
	print "Procesed " NR " records from file: " FILENAME
}
