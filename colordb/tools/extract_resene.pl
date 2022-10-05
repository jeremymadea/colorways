#!/usr/bin/env perl

sub rgb2hex { 
    return sprintf "#%02X%02X%02X", @_;
}

my %seen;

while (<>) {
    chomp;
    @F = split /\|/; 
    my $name = $F[0]; 
    my $code = $F[1]; 
    my $hex = rgb2hex($F[7], $F[8], $F[9]); 
    my $lrv = $F[10]; 
    my $note = "code($code)";
    $note .= " lrv($lrv)" unless $lrv eq '-';
    next if exists $seen{$name.$hex};
    print "resene||$name|$hex|1|$note\n";
    $seen{$name.$hex} = 1;
}
__END__
Colour name|Total Colour Code|Chart|Pencil1|Pencil2|Pencil3|Pencil4|R|G|B|LRV%
A B Sea|B47-087-258|KidzColour range (pre 2008)|152|151|-|-|51|80|131|16

CREATE TABLE colors (
    topset TEXT NOT NULL,
    subset TEXT, 
    name TEXT,
    hex TEXT,
    valid INTEGER,
    notes TEXT
);

