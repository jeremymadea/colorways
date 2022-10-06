#!/usr/bin/env perl

while(<>) {
    my ($name,$hex) = /(\S+)\s*(\S+)/;
    $hex = "#". uc $hex; 
    print "CSS3||$name|$hex|1|\n";
}


