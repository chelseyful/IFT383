#!/usr/bin/perl
# Demonstrates working with strings
$THING1 = "Hello,";
$THING2 = "World!";
$LINE = '-';
print "Using double-quotes: $THING1 $THING2\n"; # Using double quotes
print 'Using single quotes: $THING1 $THING2\n' . "\n"; # using single quptes
print "Excape sequences: \U$THING1\E\t\t\L$THING2\E\n"; # escape sequences
print $LINE x 50 . "\n"; # multiply
print length "$THING1 $THING2"; # length
print uc "\nuppercase: $THING1 $THING2\n"; # uc = uppercase
print lc "lowercase: $THING1 $THING2\n"; # uc = uppercase
print index($THING2,"!",0); # index
print "\n";
print substr($THING2,index($THING2,"!",0),1); # substring
print "\n";
