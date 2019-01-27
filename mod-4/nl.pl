#!/usr/bin/perl
@input = <STDIN>;
for ($line=0; $line < scalar @input; $line++) {
	chomp(@input[$line]);
	print $line+1 . "\t" . @input[$line] . "\n";
}
