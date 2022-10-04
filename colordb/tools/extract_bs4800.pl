#!/usr/bin/env perl
#my $sub = shift;

$text = do { undef $/, <> };

for my $row ($text =~ m!<tr>(.*?)</tr>!isg) {
    next unless $row;
    my ($hex,$code,$name) = $row =~ 
        m!(#[a-fA-F0-9]+).*?>(\w[^<]*?)<.*?>(\w.*?)<!;
    $hex = uc $hex;
    print "BS4800|extended|$name|$hex|1|$code\n";
}

__END__

<tr><td>#deded2</td><td style="background-color:#deded2"></td><td>00-A-01</td><td>Ash grey / Oyster grey / Portland</td></tr>
