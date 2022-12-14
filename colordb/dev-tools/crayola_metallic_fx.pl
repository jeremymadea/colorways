#!/usr/bin/env perl
#
# HTML code after __DATA__ token is taken from 
# https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors

my $text = do { undef $/; <DATA> };

for my $tr ($text =~ m!<tr>(.*?)</tr>!isg) {
    my ($name,$hex,$ntd) = $tr =~ m!
        <th[^>]*?>\s*(.*?)\s*</th>.*?
        (\#[A-Fa-f0-9]*)!sx;

    print "crayola|metallic-fx|$name|$hex|0|\n";

}
    
#<th scope="row">Robot Canary
#</th>
#<td>#9C7C38
#</td>
#<td>
#</td>
#<td>Known as "Metallic Sunburst" (2001–2019).
print "crayola|metallic-fx|Metallic Sunburst|#9C&C38|0|";
print "Name for Robot Canary 2001-2019.\n";


__DATA__

<tr> <td style="background:#c46210">&nbsp;
</td>
<th scope="row">Alloy Orange
</th>
<td>#C46210
</td>
<td>
</td>
<td>
</td></tr>
<tr>
<td style="background:#2e5894; color:White;">&nbsp;
</td>
<th scope="row">B'dazzled Blue
</th>
<td>#2E5894
</td>
<td>
</td>
<td>
</td></tr>
<tr>
<td style="background:#9c2542; color:White;">&nbsp;
</td>
<th scope="row">Big Dip O' Ruby
</th>
<td>#9C2542
</td>
<td>96
</td>
<td>
</td></tr>
<tr>
<td style="background:#bf4f51; color:White;">&nbsp;
</td>
<th scope="row">Bittersweet Shimmer
</th>
<td>#BF4F51
</td>
<td>
</td>
<td>
</td></tr>
<tr>
<td style="background:#a57164; color:White;">&nbsp;
</td>
<th scope="row">Blast Off Bronze
</th>
<td>#A57164
</td>
<td>
</td>
<td>
</td></tr>
<tr>
<td style="background:#58427c; color:White;">&nbsp;
</td>
<th scope="row">Cyber Grape
</th>
<td>#58427C
</td>
<td>96
</td>
<td>
</td></tr>
<tr>
<td style="background:#4a646c; color:White;">&nbsp;
</td>
<th scope="row">Deep Space Sparkle
</th>
<td>#4A646C
</td>
<td>
</td>
<td>
</td></tr>
<tr>
<td style="background:#85754e;">&nbsp;
</td>
<th scope="row">Gold Fusion
</th>
<td>#85754E
</td>
<td>
</td>
<td>
</td></tr>
<tr>
<td style="background:#319177; color:White;">&nbsp;
</td>
<th scope="row">Illuminating Emerald
</th>
<td>#319177
</td>
<td>
</td>
<td>
</td></tr>
<tr>
<td style="background:#0a7e8c; color:White;">&nbsp;
</td>
<th scope="row">Metallic Seaweed
</th>
<td>#0A7E8C
</td>
<td>
</td>
<td>
</td></tr>
<tr>
<td style="background:#9c7c38;">&nbsp;
</td>
<th scope="row">Robot Canary
</th>
<td>#9C7C38
</td>
<td>
</td>
<td>Known as "Metallic Sunburst" (2001–2019).
</td></tr>
<tr>
<td style="background:#8d4e85; color:White;">&nbsp;
</td>
<th scope="row">Razzmic Berry
</th>
<td>#8D4E85
</td>
<td>
</td>
<td>
</td></tr>
<tr>
<td style="background:#8fd400;">&nbsp;
</td>
<th scope="row">Sheen Green
</th>
<td>#8FD400
</td>
<td>96
</td>
<td>
</td></tr>
<tr>
<td style="background:#d98695;">&nbsp;
</td>
<th scope="row">Shimmering Blush
</th>
<td>#D98695
</td>
<td>
</td>
<td>
</td></tr>
<tr>
<td style="background:#757575;">&nbsp;
</td>
<th scope="row">Sonic Silver
</th>
<td>#757575
</td>
<td>
</td>
<td>
</td></tr>
<tr>
<td style="background:#0081ab; color:White;">&nbsp;
</td>
<th scope="row">Steel Blue
</th>
<td>#0081AB
</td>
<td>96
</td>
<td>
</td></tr>
<tr>
<td style="background:#c89f56;">&nbsp;
</td>
<th scope="row">Cheese Grater
</th>
<td>#C89F56
</td>
<td>
</td>
<td rowspan="8">Introduced in 2019.
</td></tr>
<tr>
<td style="background:#184FA1;">&nbsp;
</td>
<th scope="row">Iron Indigo
</th>
<td>#184FA1
</td>
<td>
</td></tr>
<tr>
<td style="background:#BF3981;">&nbsp;
</td>
<th scope="row">Magnetic Magenta
</th>
<td>#BF3981
</td>
<td>
</td></tr>
<tr>
<td style="background:#028AAE;">&nbsp;
</td>
<th scope="row">Cobalt Cool
</th>
<td>#028AAE
</td>
<td>
</td></tr>
<tr>
<td style="background:#5CB2C5;">&nbsp;
</td>
<th scope="row">Acid Wash Jeans
</th>
<td>#5CB2C5
</td>
<td>
</td></tr>
<tr>
<td style="background:#005B39;">&nbsp;
</td>
<th scope="row">Petrified Forest
</th>
<td>#005B39
</td>
<td>
</td></tr>
<tr>
<td style="background:#C88CA4;">&nbsp;
</td>
<th scope="row">Rose Gold
</th>
<td>#C88CA4
</td>
<td>
</td></tr>
<tr>
<td style="background:#C5BC42;">&nbsp;
</td>
<th scope="row">Gold Medal
</th>
<td>#C5BC42
</td>
<td>
</td></tr></tbody>


