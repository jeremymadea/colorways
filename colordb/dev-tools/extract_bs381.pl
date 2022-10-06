#!/usr/bin/env perl
#my $sub = shift;

$text = do { undef $/, <> };

for my $row ($text =~ m!<tr>(.*?)</tr>!isg) {
    next unless $row;
    my ($hex,$code,$name) = $row =~ 
        m!(#[a-fA-F0-9]+).*?>(\d+\s+\d+).*?>(\w.*?)<!;
    print "BS381||$name|$hex|1|$code\n";
}

__END__
<tr><td>#94bfac</td><td style="background-color:#94bfac;width:40%"></td><td>381 101</td><td>Sky blue</td></tr>
