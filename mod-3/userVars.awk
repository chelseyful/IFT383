BEGIN {
	print "var="var
}
/./ {
	print "var="var
}
END {
	print "var="var
}
