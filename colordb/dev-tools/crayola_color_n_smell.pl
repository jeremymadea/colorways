#!/usr/bin/env perl
#
# HTML code after __DATA__ token is taken from 
# https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors
# Manual modifications have beem made for easier parsing.

my $text = do { undef $/; <DATA> };

for my $td ($text =~ m!(<td.*?</td>)!isg) {
    my ($hex) = $td =~ /(#[A-Fa-f0-9]*)/;
    my ($name) = $td =~ m!>\s*(.*?)\s*\(!;
    my ($note) = $td =~ m!\((.*)\)!;

    print "crayola|color-n-smell|$name|$hex|0|$note\n";
}


__DATA__

<td style="background:#FFFFFF; border-bottom:0; width:12%;">Baby's Powder (White)
</td>
<td style="background:#E97451; border-bottom:0; width:12%;">Baseball Mitt (Burnt Sienna)
</td>
<td style="background:#FC80A5; border-bottom:0; width:12%;">Bubble Bath (Tickle Me Pink)
</td>
<td style="background:#C62D42; color: #fff; border-bottom:0; width:12%;">Earthworm (Brick Red)
</td>
<td style="background:#C9A0DC; border-bottom:0;">Flower Shop (Wisteria)
</td>
<td style="background:#76D7EA; border-bottom:0;">Fresh Air (Sky Blue)
</td>
<td style="background:#FF8833; border-bottom:0;">Grandma's Perfume (Orange)
</td>
<td style="background:#29AB87; border-bottom:0;">Koala Tree (Jungle Green)
</td>
<td style="background:#000000; border-bottom:0; color:white">New Sneakers (Black)
</td>
<td style="background:#AF593E; color: #fff; border-bottom:0;">Pet Shop (Brown)
</td>
<td style="background:#01796F; color: #fff; border-bottom:0;">Pine Tree (Pine Green)
</td>
<td style="background:#FFCBA4; border-bottom:0;">Saw Dust (Peach)
</td>
<td style="background:#FCD667; border-bottom:0;">Sharpening Pencils (Goldenrod)
</td>
<td style="background:#ED0A3F; color: #fff; border-bottom:0;">Smell the Roses (Red)
</td>
<td style="background:#FBE870; border-bottom:0;">Sunny Day (Yellow)
</td>
<td style="background:#FED85D; border-bottom:0;">Wash the Dog (Dandelion)
</td>


