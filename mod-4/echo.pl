#!/usr/bin/perl
use constant SEP => "-";
$INPUT=<STDIN>;
print "input without calling chomp:\n";
print SEP . $INPUT . SEP . "\n";
print "input after calling chomp:\n";
chomp($INPUT);
print SEP . $INPUT . SEP . "\n";
