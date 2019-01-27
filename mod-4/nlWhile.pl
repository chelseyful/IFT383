#!/usr/bin/perl
$LINE=1;
while (<>) {
	chomp;
	print $LINE . "\t" . $_ . "\n";
	$LINE++;
}
