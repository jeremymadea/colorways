#!/usr/bin/env perl
#my $sub = shift;

$text = do { undef $/, <> };

for my $row ($text =~ m!<tr>(.*?)</tr>!isg) {
    next unless $row;
    my ($hex,$name) = $row =~ 
        m!(#[a-fA-F0-9]+).*?>(\w.*?)<!;
    $hex = uc $hex;
    print "NBC-ISCC||$name|$hex|1|\n";
}

__END__

<tr><td>#ffb5ba</td><td style="background-color:#ffb5ba"></td><td>Vivid_Pink</td></tr>
