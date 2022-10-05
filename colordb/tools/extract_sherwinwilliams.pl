#!/usr/bin/env perl

sub rgb2hex { 
    return sprintf "#%02X%02X%02X", @_;
}

my %seen;

while (<>) {
    next unless /<button/;
    my ($label) = /aria-label="(.*?)"/;
    my ($code, $name) = $label =~ /(SW \d+)\s+([^"]*)/;
    my ($r,$g,$b) = /rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)/;
    my $hex = rgb2hex($r,$g,$b);
    print "SherwinWilliams||$name|$hex|1|$code\n";
}
__END__

<button class="color-swatch color-swatch-flat" aria-label="SW 6840 Exuberant Pink" style="height: 14.9846px; left: 0px; position: absolute; top: 0px; width: 14.9846px; background: rgb(181, 77, 127);"></button>

CREATE TABLE colors (
    topset TEXT NOT NULL,
    subset TEXT, 
    name TEXT,
    hex TEXT,
    valid INTEGER,
    notes TEXT
);

