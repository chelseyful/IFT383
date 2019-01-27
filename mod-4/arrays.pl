#!/usr/bin/perl
$INPUT = <STDIN>;
chomp($INPUT);
@things = split(/,/, $INPUT);
print "You entered " . scalar @things . " things\n";
print "The first thing was: " . @things[0] . "\n";
print "The last thing was: " . @things[(scalar @things) - 1] . "\n";
print "If I add one more thing...\n";
push(@things, "another thing!");
print "There are now " . scalar @things . " and they are...\n";
print join("\n", @things) . "\n";
