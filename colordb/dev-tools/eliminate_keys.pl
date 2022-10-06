#!/usr/bin/env perl

my $elims = shift; 

open my $elimlist, $elims or die $!; 

my %elims; 
while (<$elimlist>) { 
    chomp; 
    $elims{$_} = 1; 
}

while (<>) { 
    if (/hex2rgb/) {
        my ($k) = /([\w-]+)/;
        if (exists $elims{$k}) {
            next;
        }
    }
    print;
}
