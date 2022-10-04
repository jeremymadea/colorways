#!/usr/bin/env perl

while (<>) {
    my ($name, $hex) = /(\S.*?)\t(#[a-zA-Z0-9]*)/;
    $name =~ s!\W+!-!g;
    $hex = uc $hex;

    print "xkcd||$name|$hex|1|\n"
}
