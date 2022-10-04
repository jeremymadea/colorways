#!/usr/bin/env perl
#my $sub = shift;

$text = do { undef $/, <> };

for my $row ($text =~ m!<tr(.*?)</tr>!isg) {
    next unless $row;
    my ($name,$hex) = $row =~ 
        m!<td>([^<]*)</td><td>(#[a-fA-F0-9]+)!i;
    next unless $hex; 
    $hex = uc $hex;
    $name =~ s/\s+/ /g;
    print "FS595|ANA|$name|$hex|1|\n";
}

__END__

<tbody><tr><th>Color Name</th><th style="width:100px">Hex</th></tr>
<tr style="color:#fff;background-color:#09568d"><td>(w3-ana-501) Blue</td><td>#09568d</td></tr>
