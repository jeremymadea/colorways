#!/usr/bin/env perl
#
# HTML code after __DATA__ token is taken from 
# https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors
# Manually modified for easier parsing. 

my $text = do { undef $/; <DATA> };

for my $td ($text =~ m!(<td[^>]*>.*?</td>)!isg) {
    my($hex) = $td =~ m!(#[A-Fa-f0-9]*)!;
    my($name) = $td =~ m!>\s*([^<]*?)\s*<!;

    print "crayola|neon|$name|$hex|0|\n";
}


__DATA__

<td style="background:#76D7EA; border-bottom:0; width:12%;">Sky Blue
</td>
<td style="background:#66FF66; border-bottom:0; width:12%;">Screamin' Green
</td>
<td style="background:#FFCC33; border-bottom:0; width:12%;">Sunglow
</td>
<td style="background:#FD5B78; border-bottom:0; width:12%;">Wild Watermelon
</td>
<td style="background:#FF00CC; border-bottom:0; width:12%;">Purple Pizzazz
</td>
<td style="background:#FFFF66; border-bottom:0; width:12%;">Laser Lemon
</td>
<td style="background:#FF9966; border-bottom:0; width:12%;">Atomic Tangerine
</td>
<td style="background:#FF6EFF; border-bottom:0; width:12%;">Shocking Pink
</td>
<td style="background:#77D8EB; border-bottom:0; width:12%;">Pearl Sky Blue
</td>
<td style="background:#67FE67; border-bottom:0; width:12%;">Pearl Screamin' Green
</td>
<td style="background:#FECD34; border-bottom:0; width:12%;">Pearl Sunglow
</td>
<td style="background:#FE5C79; border-bottom:0; width:12%;">Pearl Wild Watermelon
</td>
<td style="background:#FE01CD; border-bottom:0; width:12%;">Pearl Purple Pizzazz
</td>
<td style="background:#FEFE67; border-bottom:0; width:12%;">Pearl Laser Lemon
</td>
<td style="background:#FEA067; border-bottom:0; width:12%;">Pearl Atomic Tangerine
</td>
<td style="background:#FE6FFE; border-bottom:0; width:12%;">Pearl Shocking Pink
</td>
