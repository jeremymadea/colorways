#!/usr/bin/env perl
#my $sub = shift;

$text = do { undef $/, <> };

for my $row ($text =~ m!<tr(.*?)</tr>!isg) {
    next unless $row;
    my ($code,$name,$hex) = $row =~ 
        m!<td>([^<]*)</td><td>([^<]*)</td>.*?<td>.*(#[a-fA-F0-9]+)!si;
    next unless $hex; 
    $hex = uc $hex;
    $name =~ s/^\s+//g;
    $name =~ s/\s+/ /g;
    $code =~ s/[()]//g;
    print "FS595|safety|$name|$hex|1|$code\n";
}

__END__

<tbody><tr><th style="width:80px">Number</th><th>Name</th><th style="width:90px">Hex</th></tr>
<tr style="color:#fff;background-color:#bd1e24"><td>(11120)</td><td>w3-safety-red</td>
<td><a href="colors_picker.asp?color=%23bd1e24">#bd1e24</a></td></tr>
