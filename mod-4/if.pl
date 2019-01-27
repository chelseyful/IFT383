#!/usr/bin/perl
$VAR1=100;
$VAR2=50;
if ($VAR1 > $VAR2) {
	print $VAR1 . " is greater than " . $VAR2 . "\n";
} elsif ($VAR1 < $VAR2) {
	print $VAR1 . " is less than " . $VAR2 . "\n";
} else {
	print $VAR1 . " is equal to " . $VAR2 . "\n";
}

print "something, something, something...\n" if ($VAR2==50);
print "another something\n" if ($VAR2!=50);
