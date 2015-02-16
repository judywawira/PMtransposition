#!/usr/bin/perl

use strict;

die "Please supply an input file name.\n" if !$ARGV[0];

my $transposed;
my $fntomid;
my $lntofn;
my $lntomid;
my $rec;
my @a;
my $fn1;
my $fn2;
my $ln1;
my $ln2;
my $mid1;
my $mid2;

open (I, "$ARGV[0]") or die "Can't open $ARGV[0]\n";
open (O, ">$ARGV[0].out") or die "Can't open $ARGV[0]\n";

# These column numbers are based on the file originally created by James Egg
# and entitled "new_output_with_header.txt"

my $fn_col = 28; # (zero based)
my $mid_col = 30; # (zero based)
my $ln_col = 32; # (zero based)

while ($rec = <I>) {

    $transposed = 0;
    $fntomid = 0;
    $lntofn = 0;
    $lntomid = 0;

    $rec =~ s/\s+$//;

    @a = split/\|/,$rec;

    $fn1 = $a[$fn_col];
    $fn2 = $a[$fn_col+1];

    $ln1 = $a[$ln_col];
    $ln2 = $a[$ln_col+1];

    $mid1 = $a[$mid_col];
    $mid2 = $a[$mid_col+1];

#    print "$fn1\|$fn2\|$mid1\|$mid2\|$ln1\|$ln2\n";

    #fn to mid
    if ( ($fn1 eq $mid2 and $fn1 ne "" and $mid2 ne "" and $mid1 ne $mid2 and $fn1 ne $fn2) or ($fn2 eq $mid1 and $fn2 ne "" and $mid1 ne "" and $mid1 ne $mid2 and $fn1 ne $fn2) ) {
	$transposed = 1;
	$fntomid = 1;
    }
	
    # ln to fn
    if ( ($ln1 eq $fn2 and $ln1 ne "" and $fn2 ne "" and $fn1 ne $fn2 and $ln1 ne $ln2) or ($ln2 eq $fn1 and $ln2 ne "" and $fn1 ne "" and $fn1 ne $fn2 and $ln1 ne $ln2) ) {
	$transposed = 1;
	$lntofn = 1;
    }

    #ln to mid
    if ( ($ln1 eq $mid2 and $ln1 ne "" and $mid2 ne "" and $mid1 ne $mid2 and $ln1 ne $ln2) or ($ln2 eq $mid1 and $ln2 ne "" and $mid1 ne "" and $mid1 ne $mid2 and $ln1 ne $ln2) ) {
	$transposed = 1;
	$lntomid = 1;
    }

    print O $rec, "\|$transposed\|$fntomid\|$lntofn\|$lntomid\n";

}
