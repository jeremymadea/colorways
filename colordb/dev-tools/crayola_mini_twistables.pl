#!/usr/bin/env perl
#
# HTML code after __DATA__ token is taken from 
# https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors

my $text = do { undef $/; <DATA> };

for my $tr ($text =~ m!<tr[^>]*>(.*?)</tr>!isg) {

    my($name) = $tr =~ m!<td>\s*(\w.*\S?)\s*<!;
    my($hex) = $tr =~ m!(#[A-Fa-f0-9]*)!;

    print "crayola|mini-twistables|$name|$hex|0|\n";
}


__DATA__

<tr>
<td style="background:#fdd9b5;">&nbsp;
</td>
<td>Apricot
</td>
<td>#FDD9B5
</td></tr>
<tr>
<td style="background:#000000; color:white;">&nbsp;
</td>
<td>Black
</td>
<td>#000000
</td></tr>
<tr>
<td style="background:#1f75fe; color:white;">&nbsp;
</td>
<td>Blue
</td>
<td>#1F75FE
</td></tr>
<tr>
<td style="background:#0d98ba;">&nbsp;
</td>
<td>Blue Green
</td>
<td>#0D98BA
</td></tr>
<tr>
<td style="background:#7366bd;">&nbsp;
</td>
<td>Blue Violet
</td>
<td>#7366BD
</td></tr>
<tr>
<td style="background:#b4674d;">&nbsp;
</td>
<td>Brown
</td>
<td>#B4674D
</td></tr>
<tr>
<td style="background:#ffaacc;">&nbsp;
</td>
<td>Carnation Pink
</td>
<td>#FFAACC
</td></tr>
<tr>
<td style="background:#1dacd6;">&nbsp;
</td>
<td>Cerulean
</td>
<td>#1DACD6
</td></tr>
<tr>
<td style="background:#fddb6d;">&nbsp;
</td>
<td>Dandelion
</td>
<td>#FDDB6D
</td></tr>
<tr>
<td style="background:#95918c;">&nbsp;
</td>
<td>Gray
</td>
<td>#95918C
</td></tr>
<tr>
<td style="background:#1cac78;">&nbsp;
</td>
<td>Green
</td>
<td>#1CAC78
</td></tr>
<tr>
<td style="background:#f0e891;">&nbsp;
</td>
<td>Green Yellow
</td>
<td>#F0E891
</td></tr>
<tr>
<td style="background:#5d76cb;">&nbsp;
</td>
<td>Indigo
</td>
<td>#5D76CB
</td></tr>
<tr>
<td style="background:#ff7538;">&nbsp;
</td>
<td>Orange
</td>
<td>#FF7538
</td></tr>
<tr>
<td style="background:#ee204d;">&nbsp;
</td>
<td>Red
</td>
<td>#EE204D
</td></tr>
<tr>
<td style="background:#ff5349;">&nbsp;
</td>
<td>Red Orange
</td>
<td>#FF5349
</td></tr>
<tr>
<td style="background:#c0448f;">&nbsp;
</td>
<td>Red Violet
</td>
<td>#C0448F
</td></tr>
<tr>
<td style="background:#fc2847;">&nbsp;
</td>
<td>Scarlet
</td>
<td>#FC2847
</td></tr>
<tr>
<td style="background:#926eae; color:white;">&nbsp;
</td>
<td>Violet (Purple)
</td>
<td>#926EAE
</td></tr>
<tr>
<td style="background:#f75394;">&nbsp;
</td>
<td>Violet Red
</td>
<td>#F75394
</td></tr>
<tr>
<td style="background:#ffffff;">&nbsp;
</td>
<td>White
</td>
<td>#FFFFFF
</td></tr>
<tr>
<td style="background:#fce883;">&nbsp;
</td>
<td>Yellow
</td>
<td>#FCE883
</td></tr>
<tr>
<td style="background:#c5e384;">&nbsp;
</td>
<td>Yellow Green
</td>
<td>#C5E384
</td></tr>
<tr>
<td style="background:#ffae42;">&nbsp;
</td>
<td>Yellow Orange
</td>
<td>#FFAE42
</td></tr>


