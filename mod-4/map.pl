#!/usr/bin/perl
%myMap = (
	"sleep" => "ZzzZzzZzz...",
	"eat" => "Om nom nom!",
	"read" => "You read a short story...",
	"watch" => "You watch a documentary about Liamas"
);
$myMap{"homework"} = "You get all your homework done! YAY!";
@keys = keys(%myMap);
print "please enter one of the following ways to spend Saturday morning:\n\n";
print join("\n",@keys) . "\n";
$response=<STDIN>;
chomp($response);
print $myMap{$response} . "\n";
