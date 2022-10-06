#!/usr/bin/env perl
#
# HTML code after __DATA__ token is taken from 
# https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors
# Manual modification have been made for easier parsing. 


my $text = do { undef $/; <DATA> };

for my $td ($text =~ m!(<td.*?</td>)!isg) {
    my ($hex) = $td =~ /(#[A-Fa-f0-9]*)/;
    my ($name) = $td =~ m!>\s*(.*?)\s*\(!; 
    my ($note) = $td =~ m!\((.*)\)!; 

    print "crayola|magic-scent|$name|$hex|0|$note\n";
}


__DATA__

<td style="background:#FFFFFF; border-bottom:0; width:12%;">Baby Powder (White)
</td>
<td style="background:#FED85D; border-bottom:0; width:12%;">Banana (Dandelion)
</td>
<td style="background:#4570E6; color: white; border-bottom:0; width:12%;">Blueberry (Blue (II))
</td>
<td style="background:#FC80A5; border-bottom:0; width:12%;">Bubble Gum (Tickle Me Pink)
</td>
<td style="background:#CA3435; color:white; border-bottom:0;">Cedar Chest (Mahogany)
</td>
<td style="background:#C32148; color:white; border-bottom:0;">Cherry (Maroon)
</td>
<td style="background:#AF593E; color: white; border-bottom:0;">Chocolate (Brown)
</td>
<td style="background:#FFFFFF; border-bottom:0;">Coconut (White)
</td>
<td style="background:#FBE870; border-bottom:0;">Daffodil (Yellow)
</td>
<td style="background:#9E5B40; color:white; border-bottom:0;">Dirt (Sepia)
</td>
<td style="background:#29AB87; border-bottom:0;">Eucalyptus (Jungle Green)
</td>
<td style="background:#76D7EA; border-bottom:0;">Fresh Air (Sky Blue)
</td>
<td style="background:#8359A3; color:white; border-bottom:0;">Grape (Violet)
</td>
<td style="background:#FF8833; border-bottom:0;">Jelly Bean (Orange)
</td>
<td style="background:#000000; color:white; border-bottom:0;">Leather Jacket (Black)
</td>
<td style="background:#FBE870; border-bottom:0;">Lemon (Yellow)
</td>
<td style="background:#000000; color:white; border-bottom:0;">Licorice (Black)
</td>
<td style="background:#C9A0DC; border-bottom:0;">Lilac (Wisteria)
</td>
<td style="background:#C5E17A; border-bottom:0;">Lime (Yellow Green)
</td>
<td style="background:#FDD5B1; border-bottom:0;">Lumber (Apricot)
</td>
<td style="background:#0066FF; color:white; border-bottom:0;">New Car (Blue (III))
</td>
<td style="background:#FF8833; border-bottom:0;">Orange
</td>
<td style="background:#FFCBA4; border-bottom:0;">Peach
</td>
<td style="background:#01796F; color:white; border-bottom:0;">Pine (Pine Green)
</td>
<td style="background:#ED0A3F; color: white; border-bottom:0;">Rose (Red)
</td>
<td style="background:#FFA6C9; border-bottom:0;">Shampoo (Carnation Pink)
</td>
<td style="background:#8B8680; color:white; border-bottom:0;">Smoke (Gray)
</td>
<td style="background:#C3CDE6; border-bottom:0;">Soap (Periwinkle)
</td>
<td style="background:#FF3399; color: white; border-bottom:0;">Strawberry (Wild Strawberry)
</td>
<td style="background:#FF8833; border-bottom:0;">Tulip (Orange)
</td>
