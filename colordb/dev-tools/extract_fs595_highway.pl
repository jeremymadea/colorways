#!/usr/bin/env perl
#my $sub = shift;

$text = do { undef $/, <> };

for my $row ($text =~ m!<tr(.*?)</tr>!isg) {
    next unless $row;
    my ($code,$name,$hex) = $row =~ 
        m!<td>([^<]*)</td><td>([^<]*)</td><td>.*(#[a-fA-F0-9]+)!si;
    next unless $hex; 
    $hex = uc $hex;
    $name =~ s/^\s+//g;
    $name =~ s/\s+/ /g;
    $code =~ s/[()]//g;
    print "FS595|highway|$name|$hex|1|$code\n";
}

__END__

<tbody><tr><th style="width:80px">Number</th><th>Name</th><th style="width:90px">Hex</th></tr>
<tr style="color:#fff;background-color:#633517"><td>(10055)</td><td>w3-highway-brown</td><td>
<a href="colors_picker.asp?color=%23633517">#633517</a></td></tr>
