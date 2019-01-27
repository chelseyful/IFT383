#!/usr/bin/perl
# Demonstrates use of strict and variable scoping
use strict; # enables strict mode using the 'strict' pragma
my $VARIABLE;
$VARIABLE = "Hello, World!";
print $VARIABLE . "\n";
{
	my $VARIABLE2="Goodbye!"
}
print $VARIABLE2 . "\n";
