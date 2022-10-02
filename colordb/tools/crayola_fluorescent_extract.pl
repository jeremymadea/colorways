#!/usr/bin/env perl

$text = do { undef $/, <> };

for my $row ($text =~ m!<tr>(.*?)</tr>!sg) {
    my ($td1, $td2, $td3, $td4, $td5) = $row =~ m!
        .*?(<td.*?>.*?</td>) 
        .*?(<td.*?>.*?</td>) 
        .*?(<td.*?>.*?</td>) 
        .*?(<td.*?>.*?</td>) !xims;

    my ($hex) = $td1 =~ /(#[A-Fa-f0-9]{6})/;
    my ($name) = $td2 =~ m!>\s*(.*?)\s*<!s;
    my ($h2)   = $td3 =~ m!>\s*(#[A-Fa-f0-9]{6}).*?<!s;
    my $valid = ($h2 eq $hex);
    my ($notes) = $td4 =~ m!>(.*?)<!s;
    $notes =~ s/\s/ /g;
    $notes =~ s/'/'\\\''/eg;
    $notes =~ s/"/'\\"'/eg;
    $notes =~ s/,/'\\,'/eg;
    print "crayola|fluorescent|$name|$hex|",$valid?1:0,"|$notes\n";

}

__END__
<tr>
<td style="background: #FF355E">&nbsp;
</td>
<td>Radical Red
</td>
<td align="center" style="background:#E9E9E9">#FF355E<sup id="cite_ref-CEC_2-1" class="reference"><a href="#cite_note-CEC-2">[1]</a></sup>
</td>
<td>Introduced in 1990.
</td></tr>
<tr>
<td style="background: #FD5B78">&nbsp;
</td>
<td>Wild Watermelon
</td>
<td align="center" style="background:#E9E9E9">#FD5B78<sup id="cite_ref-CEC_2-2" class="reference"><a href="#cite_note-CEC-2">[1]</a></sup>
</td>
<td>Same color as "Ultra Red" (1972–1990).
</td></tr>
