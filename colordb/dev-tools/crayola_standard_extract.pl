#!/usr/bin/env perl

$text = do { undef $/, <> };

for my $row ($text =~ m!<tr>(.*?)</tr>!sg) {
    my ($td1, $td2, $td3, $td4, $td5) = $row =~ m!
        .*?(<td.*?>.*?</td>) 
        .*?(<td.*?>.*?</td>) 
        .*?(<td.*?>.*?</td>) 
        .*?(<td.*?>.*?</td>) 
        .*?(<td.*?>.*?</td>) !xims;

    my ($hex) = $td1 =~ /(#[A-Fa-f0-9]{6})/;
    my ($name) = $td2 =~ m!>\s*(.*?)\s*<!s;
    my ($h2)   = $td3 =~ m!>\s*(.*?)\s<*!s;
    my $valid = ($h2 eq $hex);
    my ($n1) = $td4 =~ m!>(.*?)<!s;
    my ($n2) = $td5 =~ m!>(.*?)<!s;
    $n1 =~ s/\s/ /g;
    $n2 =~ s/\s/ /g;
    my $notes = $n1 . " " . $n2;
    $notes =~ s/'/'\\\''/eg;
    $notes =~ s/"/'\\"'/eg;
    $notes =~ s/,/'\\,'/eg;
    print "crayola|standard|$name|$hex|",$valid?1:0,"|$notes\n";

}

__END__

<td style="background: #ED0A3F; color: white">&nbsp;
</td>

<td>Red
</td>

<td align="center" style="background:#E9E9E9">#ED0A3F
</td>

<td>1903–present
</td>

<td>
</td>
<td style="background:#9EFF9E;vertical-align:middle;text-align:center;" class="table-yes">Yes
</td>
<td style="background:#9EFF9E;vertical-align:middle;text-align:center;" class="table-yes">Yes
</td>
<td style="background:#9EFF9E;vertical-align:middle;text-align:center;" class="table-yes">Yes
</td>
<td style="background:#9EFF9E;vertical-align:middle;text-align:center;" class="table-yes">Yes
</td>

