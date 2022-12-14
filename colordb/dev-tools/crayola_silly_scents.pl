#!/usr/bin/env perl
#
# HTML code after __DATA__ token is taken from 
# https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors

my $text = do { undef $/; <DATA> };

for my $tr ($text =~ m!<tr[^>]*>(.*?)</tr>!isg) {
    my($hex) = $tr =~ m!(#[A-Fa-f0-9]*)!; 
    my($name,$note) = $tr =~ m!<td>(\w.*?\w)\s*</td>\s*?<td>(\w.*?\w)\s*</td>!;
    print "crayola|silly-scents|$name|$hex|0|$note\n";
}


__DATA__

<tbody>
<tr>
<td style="background:#C5E17A">&nbsp;
</td>
<td>Alien Armpit
</td>
<td>Yellow Green
</td>
<td>#C5E17A
</td></tr>
<tr>
<td style="background:#D99A6C; color:White;">&nbsp;
</td>
<td>Big Foot Feet
</td>
<td>Tan
</td>
<td>#D99A6C
</td></tr>
<tr>
<td style="background:#ECEBBD; color:White;">&nbsp;
</td>
<td>Booger Buster
</td>
<td>Spring Green
</td>
<td>#ECEBBD
</td></tr>
<tr>
<td style="background:#C32148; color:White;">&nbsp;
</td>
<td>Dingy Dungeon
</td>
<td>Maroon
</td>
<td>#C32148
</td></tr>
<tr>
<td style="background:#FED85D; color:White;">&nbsp;
</td>
<td>Gargoyle Gas
</td>
<td>Dandelion
</td>
<td>#FED85D
</td></tr>
<tr>
<td style="background:#B94E48; color:White;">&nbsp;
</td>
<td>Giant's Club
</td>
<td>Chestnut
</td>
<td>#B94E48
</td></tr>
<tr>
<td style="background:#ED0A3F; color:White;">&nbsp;
</td>
<td>Magic Potion
</td>
<td>Red
</td>
<td>#ED0A3F
</td></tr>
<tr>
<td style="background:#8B8680;">&nbsp;
</td>
<td>Mummy's Tomb
</td>
<td>Gray
</td>
<td>#8B8680
</td></tr>
<tr>
<td style="background:#FF681F; color:White;">&nbsp;
</td>
<td>Ogre Odor
</td>
<td>Red Orange
</td>
<td>#FF681F
</td></tr>
<tr>
<td style="background:#6456B7; color:White;">&nbsp;
</td>
<td>Pixie Powder
</td>
<td>Blue Violet
</td>
<td>#6456B7
</td></tr>
<tr>
<td style="background:#FC80A5;">&nbsp;
</td>
<td>Princess Perfume
</td>
<td>Tickle Me Pink
</td>
<td>#FC80A5
</td></tr>
<tr>
<td style="background:#F7468A; color:White;">&nbsp;
</td>
<td>Sasquatch Socks
</td>
<td>Violet Red
</td>
<td>#F7468A
</td></tr>
<tr>
<td style="background:#00CCCC;">&nbsp;
</td>
<td>Sea Serpent
</td>
<td>Robin's Egg Blue
</td>
<td>#00CCCC
</td></tr>
<tr>
<td style="background:#FF8833;">&nbsp;
</td>
<td>Smashed Pumpkin
</td>
<td>Orange
</td>
<td>#FF8833
</td></tr>
<tr>
<td style="background:#E77200;">&nbsp;
</td>
<td>Sunburnt Cyclops
</td>
<td>Mango Tango
</td>
<td>#E77200
</td></tr>
<tr>
<td style="background:#76D7EA; color:White;">&nbsp;
</td>
<td>Winter Wizard
</td>
<td>Sky Blue
</td>
<td>#76D7EA
</td></tr></tbody>


