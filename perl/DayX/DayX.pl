#!/usr/bin/env perl
# DayX.pl
#
# First attempt at doing Day X of Advent of Code 2025 with perl.

use warnings;
use strict;

# Setup an empty array
my @array;
my @array_output;
# Open the file, remove \n and then put into array
open( my $fh, "<", "DayX_input.txt")
#open(my $fh, "<", "DayX_test_input.txt")
    or die "Failed to open file : $!\n";
while(<$fh>) {
    chomp;
    push @array, $_;
}
close $fh;

#print join " ", @array;

my $count = 0;
foreach (@array) {
#    print $_;
    if ($_ eq "") {
        $count += 1;
        $array_output[$count] = 0;
    } elsif ($_ eq "\n"){
        print "pass";
    } else {
#        print $count;
        $array_output[$count] += $_;
    }
}
# print join " ", @array_output;

my @sorted_array = sort { $a <=> $b } @array_output;
print "max: $sorted_array[-1]\n";

print "max3: $sorted_array[-1] $sorted_array[-2] $sorted_array[-3]\n";
my $val = $sorted_array[-1] + $sorted_array[-2] + $sorted_array[-3];
print "total: $val\n";
