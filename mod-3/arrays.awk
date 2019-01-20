# Use with buildings file
BEGIN {
	FS=","
}
{
	VAR["code"]=$1
	VAR["name"]=$2
	VAR["floors"]=$3
	print VAR["code"],VAR["name"],VAR["floors"]
}
END {}
