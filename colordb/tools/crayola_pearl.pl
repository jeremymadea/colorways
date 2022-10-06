#!/usr/bin/env perl
#
# HTML code after __DATA__ token is taken from 
# https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors

my $text = do { undef $/; <DATA> };

for my $tr ($text =~ m!<tr[^>]*>(.*?)</tr>!isg) {

    my ($hex) = $tr =~ m!(#[A-Fa-f0-9]*)!;
    my ($name) = $tr =~ m!<td>(\w[^<]*?)\s*<!;
    print "crayola|pearl|$name|$hex|0|\n";
}


__DATA__

<tr>
<td style="background:#9F9F9F;">
</td>
<td>Antique Gray
</td>
<td>#9F9F9F
</td></tr>
<tr>
<td style="background:#BF3F3F;">
</td>
<td>Apple Orchard
</td>
<td>#BF3F3F
</td></tr>
<tr>
<td style="background:#A43482;">
</td>
<td>Berry Parfait
</td>
<td>#A43482
</td></tr>
<tr>
<td style="background:#3A3A3A;">
</td>
<td>Black Pearl
</td>
<td>#3A3A3A
</td></tr>
<tr>
<td style="background:#DF9ACA;">
</td>
<td>Bubble Gum
</td>
<td>#DF9ACA
</td></tr>
<tr>
<td style="background:#E74F00;">
</td>
<td>Butternut Squash
</td>
<td>#E74F00
</td></tr>
<tr>
<td style="background:#67CD95;">
</td>
<td>Caribbean Sea
</td>
<td>#67CD95
</td></tr>
<tr>
<td style="background:#548CD0;">
</td>
<td>Cloudy Sky
</td>
<td>#548CD0
</td></tr>
<tr>
<td style="background:#8F482F;">
</td>
<td>Hot Cocoa
</td>
<td>#8F482F
</td></tr>
<tr>
<td style="background:#3C32CD;">
</td>
<td>Iridescent Indigo
</td>
<td>#3C32CD
</td></tr>
<tr>
<td style="background:#6B4D82;">
</td>
<td>Lavender Silk
</td>
<td>#6B4D82
</td></tr>
<tr>
<td style="background:#94DDCB;">
</td>
<td>Leafy Canopy
</td>
<td>#94DDCB
</td></tr>
<tr>
<td style="background:#FFD966;">
</td>
<td>Liquid Gold
</td>
<td>#FFD966
</td></tr>
<tr>
<td style="background:#FF6137;">
</td>
<td>Mango Puree
</td>
<td>#FF6137
</td></tr>
<tr>
<td style="background:#4F2CD0;">
</td>
<td>Moonlit Pond
</td>
<td>#4F2CD0
</td></tr>
<tr>
<td style="background:#62C9D3;">
</td>
<td>Ocean Foam
</td>
<td>#62C9D3
</td></tr>
<tr>
<td style="background:#FF8021;">
</td>
<td>Orange Peel
</td>
<td>#FF8021
</td></tr>
<tr>
<td style="background:#5F7B4A;">
</td>
<td>Pesto
</td>
<td>#5F7B4A
</td></tr>
<tr>
<td style="background:#FFB2E7;">
</td>
<td>Pink Luster
</td>
<td>#FFB2E7
</td></tr>
<tr>
<td style="background:#9F3434;">
</td>
<td>Red Satin
</td>
<td>#9F3434
</td></tr>
<tr>
<td style="background:#C4EA7F;">
</td>
<td>Sea Glass
</td>
<td>#C4EA7F
</td></tr>
<tr>
<td style="background:#FFFF65;">
</td>
<td>Shooting Star
</td>
<td>#FFFF65
</td></tr>
<tr>
<td style="background:#F3F3F3;">
</td>
<td>Snow Drift
</td>
<td>#F3F3F3
</td></tr>
<tr>
<td style="background:#F79015;">
</td>
<td>Sunset Shimmer
</td>
<td>#F79015
</td></tr></tbody>


