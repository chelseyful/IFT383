# Formats output of `ps aux` into CSV
# Filters only processes running as root
BEGIN {
	FIELDWIDTHS="8 6 5 5 7 6"
	OFS=","
}
$1~/root/ {
	print $1,$2,$3,$4,$5,$6
}
END {}
