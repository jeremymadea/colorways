#!/usr/bin/env perl

$text = do { undef $/, <> };

for my $row ($text =~ m!<tr>(.*?)</tr>!isg) {
    for my $cell ($row =~ m!(<td.*?</td>)!isg) {
        my ($hex,$name) = $cell =~ m!(#[A-Fa-f0-9]{6}).*?>\s*(.*?)\s*<!s;
        print "crayola|silverswirls|$name|$hex|0|approximated hexcode\n";
    }
}

__END__

><tr>
<td style="background:#C39953; border-bottom:0; width:12%;">Aztec Gold
</td>
<td style="background:#A17A74; border-bottom:0; width:12%;">Burnished Brown
</td>
<td style="background:#6D9BC3; border-bottom:0; width:12%;">Cerulean Frost
</td>
<td style="background:#CD607E; border-bottom:0; width:12%;">Cinnamon Satin
</td></tr>
<tr>

