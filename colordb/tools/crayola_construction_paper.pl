#!/usr/bin/env perl
#
# HTML code after __DATA__ token is taken from 
# https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors
# Modification have been made for easier parsing. 

my $text = do { undef $/; <DATA> };

for my $tr ($text =~ m!<tr[^>]*>(.*?)</tr>!isg) {
    my($hex) = $tr =~ m!(#[A-Fa-f0-9]*)!;
    my($name) = $tr =~ m!<td>\s*(\w.*?)\s*</td>!;

    print "crayola|construction-paper|$name|$hex|0|\n";
}


__DATA__

<tr> <td style="background:#e7343c;"> </td> <td>Red</td></tr>
<tr> <td style="background:#f89f31;"> </td> <td>Orange</td></tr>
<tr> <td style="background:#fdf750;"> </td> <td>Yellow</td></tr>
<tr> <td style="background:#2baf71;"> </td> <td>Green</td></tr>
<tr> <td style="background:#3050d0;"> </td> <td>Blue</td></tr>
<tr> <td style="background:#56b8fe;"> </td> <td>Sky Blue</td></tr>
<tr> <td style="background:#873de9;"> </td> <td>Purple</td></tr>
<tr> <td style="background:#ff9fff;"> </td> <td>Pink</td></tr>
<tr> <td style="background:#fecfe1;"> </td> <td>Rose</td></tr>
<tr> <td style="background:#000000;"> </td> <td>Black</td></tr>
<tr> <td style="background:#ffffff;"> </td> <td>White</td></tr>
<tr> <td style="background:#858585;"> </td> <td>Grey</td></tr>
<tr> <td style="background:#50fc3d;"> </td> <td>Electric Green</td></tr>
<tr> <td style="background:#ad2762;"> </td> <td>Maroon</td></tr>
<tr> <td style="background:#c8c8c8;"> </td> <td>Sliver</td></tr>
<tr> <td style="background:#75472a;"> </td> <td>Brown</td>


