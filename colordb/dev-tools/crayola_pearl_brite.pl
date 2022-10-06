#!/usr/bin/env perl
#
# HTML code after __DATA__ token is taken from 
# https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors
# Manual modifications have been made for easier parsing. 

my $text = do { undef $/; <DATA> };

for my $td ($text =~ m!(<td.*?</td>)!isg) {
    my ($hex) = $td =~ /(#[A-Fa-f0-9]*)/;
    my ($name) = $td =~ m!>\s*([^>\n]*)\s*</td!;
    print "crayola|pearl-brite|$name|$hex|0|\n";

}


__DATA__

<td style="background:#5FBED7; border-bottom:0; width:12%;">Aqua Pearl
</td>
<td style="background:#54626F; color:#FFFFFF; border-bottom:0; width:12%;">Black Coral Pearl
</td>
<td style="background:#6ADA8E; border-bottom:0; width:12%;">Caribbean Green Pearl
</td>
<td style="background:#F5F5F5; border-bottom:0; width:12%;">Cultured Pearl
</td>
<td style="background:#E8F48C; border-bottom:0;">Key Lime Pearl
</td>
<td style="background:#F37A48; border-bottom:0;">Mandarin Pearl
</td>
<td style="background:#702670; color:#FFFFFF; border-bottom:0;">Midnight Pearl
</td>
<td style="background:#D65282; border-bottom:0;">Mystic Pearl
</td>
<td style="background:#4F42B5; color:#FFFFFF; border-bottom:0;">Ocean Blue Pearl
</td>
<td style="background:#48BF91; border-bottom:0;">Ocean Green Pearl
</td>
<td style="background:#7B4259; color:#FFFFFF; border-bottom:0;">Orchid Pearl
</td>
<td style="background:#F03865; color: #fff; border-bottom:0;">Rose Pearl
</td>
<td style="background:#F1444A; color:#FFFFFF; border-bottom:0;">Salmon Pearl
</td>
<td style="background:#F2F27A; border-bottom:0;">Sunny Pearl
</td>
<td style="background:#F1CC79; border-bottom:0;">Sunset Pearl
</td>
<td style="background:#3BBCD0; border-bottom:0;">Turquoise Pearl
</td>


