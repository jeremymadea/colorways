#!/usr/bin/env perl

sub rgb2hex { 
    return sprintf "#%02X%02X%02X", @_;
}

while (<>) {
    my ($r, $g, $b, $name) = /(\d+)\s+(\d+)\s+(\d+)\s+(\S.*\S)/;
    $name = lc $name; 
    $name =~ s/\W+/-/g;
    $hex = rgb2hex($r,$g,$b);
    print "x11|old|$name|$hex|1|\n";
}

__END__
    topset TEXT NOT NULL,
    subset TEXT, 
    name TEXT,
    hex TEXT,
    valid INTEGER,
    notes TEXT
255 250 250		snow
