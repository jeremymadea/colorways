#!/usr/bin/env perl
#my $sub = shift;

$text = do { undef $/, <> };

for my $row ($text =~ m!<tr>(.*?)</tr>!isg) {
    next unless $row;
    my ($code,$name,$hex) = $row =~ 
        m!<td>(\w[^<]*)</td><td[^>]*>([^<]*)</td><td>(#[a-fA-F0-9]+)!i;
    next unless $hex; 
    $name =~ s/\s+/ /g;
    print "FS595C||$name|$hex|1|$code\n";
}

__END__

<tbody><tr><th style="width:50px">Number</th><th>Color Name (if any)</th><th style="width:90px">Hex</th></tr>
<tr><td>10032</td><td style="color:#fff;background-color:#2A1610"></td><td>#2a1610</td></tr>
<tr><td>10045</td><td style="color:#fff;background-color:#523F3E"></td><td>#523f3e</td></tr>
<tr><td>10049</td><td style="color:#fff;background-color:#421814">Maroon 81352, ANA 510</td><td>#421814</td></tr>
