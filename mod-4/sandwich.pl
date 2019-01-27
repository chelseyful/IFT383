#!/usr/bin/perl
sub sandwich {
	print "making a sandwitch with:\n";
	print join("\n", @_);
	print "\n";
	return 1.99 * scalar @_;
}

&sandwich("peanut butter","jelly");
print "-" x 25 . "\n";
$mySandwich = sandwich("Ham", "Turkey", "Provalone");
print 'Your total cost is: $' . $mySandwich . "\n";
