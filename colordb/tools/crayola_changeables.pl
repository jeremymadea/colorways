#!/usr/bin/env perl
#
# HTML code after __DATA__ token is taken from 
# https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors
# Manual modifications have been made for easier parsing. 

my $text = do { undef $/; <DATA> };

for my $td ($text =~ m!(<td.*?</td>)!isg) {
    my ($hex) = $td =~ /(#[A-Fa-f0-9]*)/;
    my ($name) = $td =~ m!>\s*(.*?)\s*<!;

    print "crayola|changeables|$name|$hex|0|\n";
}


__DATA__

<td style="background-color:#C0E7F1; color: #000; width:6em; border-bottom:0;">Blue
</td>
<td style="background-color:#EB58DD; color: #000; width:6em; border-bottom:0;">Magenta
</td>
<td style="background-color:#37b978; color: #000; border-bottom:0;">Green
</td>
<td style="background-color:#963D7F; color:#FFFFFF; border-bottom:0;">Violet
</td>
<td style="background-color:#FF8071; color: #000; border-bottom:0;">Orange
</td>
<td style="background-color:#000000; color:#FFFFFF; border-bottom:0;">Black
</td>
<td style="background-color:#FF8ABA; color: #000; border-bottom:0;">Pink
</td>
<td style="background-color:#FFF7CC; color: #000; border-bottom:0;">Yellow
</td>
<td style="background-color:#F4405D; color: #fff; border-bottom:0;">Red
</td>
<td style="background-color:#131391; color:#FFFFFF; border-bottom:0;">Blue
</td>
<td style="background-color:#FDFD07; color: #000; border-bottom:0;">Yellow
</td>
<td style="background-color:#4F7948; color:#FFFFFF; border-bottom:0;">Green
</td>
<td style="background-color:#FFE9D1; color: #000; border-bottom:0;" colspan="2">Color changer
</td>


