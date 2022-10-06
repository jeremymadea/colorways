#!/usr/bin/env perl

my $text = do { undef $/; <> };

for my $a ($text =~ m!(<a[^>]*>.*?</a>)!isg) {
    my ($hex) = $a =~ /(#[A-Fa-f0-9]*)/;
    my ($code) = $a =~ /number">([^<]*)/;
    my $name;
    if ($a =~ /subtext/) { 
        ($name) = $a =~ /<br>([^<]*)/;   
    }
    $name = $code unless $name;
    print "ral||$name|$hex|1|$code\n";
}

