#!/usr/bin/env perl
#
# HTML code after __DATA__ token is taken from 
# https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors
# Manually modified for easier parsing. 

my $text = do { undef $/; <DATA> };

for my $td ($text =~ m!(<td.*?</td>)!isg) {

    my($hex) = $td =~ m!(#[A-Fa-f0-9]*)!;
    my($name) = $td =~ m!>\s*(.*?)\s*<!;

    print "crayola|heads-n-tails|$name|$hex|0|\n";
}


__DATA__

<td style="background:#FF3855; border-width:2px 2px 0px 2px; width:8em;">Sizzling Red
</td>
<td style="background:#FD3A4A; border-width:2px 2px 0px 2px; width:8em;">Red Salsa
</td>
<td style="background:#FB4D46; border-width:2px 2px 0px 2px; width:8em;">Tart Orange
</td>
<td style="background:#FA5B3D; border-width:2px 2px 0px 2px; width:8em;">Orange Soda
</td>
<td style="background:#FFAA1D; border-width:2px 2px 0px 2px;">Bright Yellow
</td>
<td style="background:#FFF700; border-width:2px 2px 0px 2px;">Yellow Sunshine
</td>
<td style="background:#299617; color:#FFFFFF; border-width:2px 2px 0px 2px;">Slimy Green
</td>
<td style="background:#A7F432; border-width:2px 2px 0px 2px;">Green Lizard
</td>
<td style="background:#2243B6; border-width:2px 2px 0px 2px;">Denim Blue
</td>
<td style="background:#5DADEC; border-width:2px 2px 0px 2px;">Blue Jeans
</td>
<td style="background:#5946B2; border-width:2px 2px 0px 2px;">Plump Purple
</td>
<td style="background:#9C51B6; border-width:2px 2px 0px 2px;">Purple Plum
</td>
<td style="background:#A83731; border-width:2px 2px 0px 2px;">Sweet Brown
</td>
<td style="background:#AF6E4D; border-width:2px 2px 0px 2px;">Brown Sugar
</td>
<td style="background:#1B1B1B; border-width:2px 2px 0px 2px;">Eerie Black
</td>
<td style="background:#BFAFB2; border-width:2px 2px 0px 2px;">Black Shadows
</td>


