#!/usr/bin/env perl
#
# HTML code after __DATA__ token is taken from 
# https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors

my $text = do { undef $/; <DATA> };

for my $tr ($text =~ m!<tr[^>]*>(.*?)</tr>!isg) {

    my($hex) = $tr =~ m!(#[A-Fa-f0-9]*)!;
    my($name) = $tr =~ m!>\s*(\w[^<]+?)\s*<!;

    print "crayola|colors-of-the-world|$name|$hex|0|\n";
}


__DATA__

<tr>
<td style="background:#986A5A;">
</td>
<td>Deep Almond
</td>
<td>#986A5A
</td>
<td>24
</td></tr>
<tr>
<td style="background:#8D5B28;">
</td>
<td>Deep Golden
</td>
<td>#8D5B28
</td>
<td>24
</td></tr>
<tr>
<td style="background:#B86F69;">
</td>
<td>Deep Rose
</td>
<td>#B86F69
</td>
<td>24
</td></tr>
<tr>
<td style="background:#513529;">
</td>
<td>Deepest Almond
</td>
<td>#513529
</td>
<td>24
</td></tr>
<tr>
<td style="background:#6E5046;">
</td>
<td>Extra Deep Almond
</td>
<td>#6E5046
</td>
<td>24
</td></tr>
<tr>
<td style="background:#5F452E;">
</td>
<td>Extra Deep Golden
</td>
<td>#5F452E
</td>
<td>24
</td></tr>
<tr>
<td style="background:#6C4D4B;">
</td>
<td>Extra Deep Rose
</td>
<td>#6C4D4B
</td>
<td>24
</td></tr>
<tr>
<td style="background:#EEE6CF;">
</td>
<td>Extra Light Almond
</td>
<td>#EEE6CF
</td>
<td>24
</td></tr>

<tr>
<td style="background:#E6B9B3;">
</td>
<td>Light Almond
</td>
<td>#E6B9B3
</td>
<td>24
</td></tr>
<tr>
<td style="background:#EDDBC7;">
</td>
<td>Light Golden
</td>
<td>#EDDBC7
</td>
<td>24
</td></tr>
<tr>
<td style="background:#E0B5A4;">
</td>
<td>Light Medium Almond
</td>
<td>#E0B5A4
</td>
<td>24
</td></tr>
<tr>
<td style="background:#F0C9A2;">
</td>
<td>Light Medium Golden
</td>
<td>#F0C9A2
</td>
<td>24
</td></tr>
<tr>
<td style="background:#F4AFB2;">
</td>
<td>Light Medium Rose
</td>
<td>#F4AFB2
</td>
<td>24
</td></tr>
<tr>
<td style="background:#FAC7C3;">
</td>
<td>Light Rose
</td>
<td>#FAC7C3
</td>
<td>24
</td></tr>
<tr>
<td style="background:#D19C7D;">
</td>
<td>Medium Almond
</td>
<td>#D19C7D
</td>
<td>24
</td></tr>
<tr>
<td style="background:#AC8065;">
</td>
<td>Medium Deep Almond
</td>
<td>#AC8065
</td>
<td>24
</td></tr>
<tr>
<td style="background:#A16B4F;">
</td>
<td>Medium Deep Golden
</td>
<td>#A16B4F
</td>
<td>24
</td></tr>
<tr>
<td style="background:#EE8E99;">
</td>
<td>Medium Deep Rose
</td>
<td>#EE8E99
</td>
<td>24
</td></tr>
<tr>
<td style="background:#DEA26C;">
</td>
<td>Medium Golden
</td>
<td>#DEA26C
</td>
<td>24
</td></tr>

<tr>
<td style="background:#88605E;">
</td>
<td>Very Deep Almond
</td>
<td>#88605E
</td>
<td>24
</td></tr>
<tr>
<td style="background:#8F6C68;">
</td>
<td>Very Deep Rose
</td>
<td>#8F6C68
</td>
<td>24
</td></tr>
<tr>
<td style="background:#E6D2D3;">
</td>
<td>Very Light Almond
</td>
<td>#E6D2D3
</td>
<td>24
</td></tr>
<tr>
<td style="background:#F0DFCF;">
</td>
<td>Very Light Golden
</td>
<td>#F0DFCF
</td>
<td>24
</td></tr>
<tr>
<td style="background:#F7E1E3;">
</td>
<td>Very Light Rose
</td>
<td>#F7E1E3
</td>
<td>24
</td></tr>
<tr>
<td style="background:#000000;">
</td>
<td>Black Hair
</td>
<td>#000000
</td>
<td>32
</td></tr>
<tr>
<td style="background:#FFFF99;">
</td>
<td>Blonde Hair
</td>
<td>#FFFF99
</td>
<td>32
</td></tr>
<tr>
<td style="background:#6CDAE7;">
</td>
<td>Blue Eyes
</td>
<td>#6CDAE7
</td>
<td>32
</td></tr>
<tr>
<td style="background:#AF593E;">
</td>
<td>Brown Eyes
</td>
<td>#AF593E
</td>
<td>32
</td></tr>
<tr>
<td style="background:#9E5B40;">
</td>
<td>Brown Hair
</td>
<td>#9E5B40
</td>
<td>32
</td></tr>
<tr>
<td style="background:#7BA05B;">
</td>
<td>Green Eyes
</td>
<td>#7BA05B
</td>
<td>32
</td></tr>
<tr>
<td style="background:#D27D46;">
</td>
<td>Hazel Eyes
</td>
<td>#D27D46
</td>
<td>32
</td></tr>
<tr>
<td style="background:#CA3435;">
</td>
<td>Red Hair
</td>
<td>#CA3435
</td>
<td>32
</td></tr>
</tbody>


