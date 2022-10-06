#!/usr/bin/env perl
#
# HTML code after __DATA__ token is taken from 
# https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors
# Manual modifications have been made for easier parsing. 

my $text = do { undef $/; <DATA> };

for my $td ($text =~ m!(<td.*?</td>)!isg) {
    my ($hex) = $td =~ /(#[A-Fa-f0-9]*)/;
    my ($name) = $td =~ m!>\s*([^>]*)\s*</span!;
    print "crayola|gem-tones|$name|$hex|0|\n";

}

__DATA__

<td style="background:#64609A; border-bottom:0; width:12%;"><a href="/wiki/Amethyst" title="Amethyst"><span style="color: white; text-decoration: inherit;">Amethyst</span></a>
</td>
<td style="background:#933709; border-bottom:0; width:12%;"><a href="/wiki/Citrine_quartz" class="mw-redirect" title="Citrine quartz"><span style="color: white; text-decoration: inherit;">Citrine</span></a>
</td>
<td style="background:#14A989; border-bottom:0; width:12%;"><a href="/wiki/Emerald" title="Emerald"><span style="color: white; text-decoration: inherit;">Emerald</span></a>
</td>
<td style="background:#469A84; border-bottom:0; width:12%;"><a href="/wiki/Jade" title="Jade"><span style="color: white; text-decoration: inherit;">Jade</span></a>
</td>
<td style="background:#D05340; border-bottom:0;"><a href="/wiki/Jasper" title="Jasper"><span style="color: white; text-decoration: inherit;">Jasper</span></a>
</td>
<td style="background:#436CB9; border-bottom:0;"><a href="/wiki/Lapis_Lazuli" class="mw-redirect" title="Lapis Lazuli"><span style="color: white; text-decoration: inherit;">Lapis Lazuli</span></a>
</td>
<td style="background:#469496; border-bottom:0;"><a href="/wiki/Malachite" title="Malachite"><span style="color: white; text-decoration: inherit;">Malachite</span></a>
</td>
<td style="background:#3AA8C1; border-bottom:0;"><a href="/wiki/Moonstone_(gemstone)" title="Moonstone (gemstone)"><span style="color: white; text-decoration: inherit;">Moonstone</span></a>
</td>
<td style="background:#353839; border-bottom:0;"><a href="/wiki/Onyx_(color)" class="mw-redirect" title="Onyx (color)"><span style="color: white; text-decoration: inherit;">Onyx</span></a>
</td>
<td style="background:#ABAD48; border-bottom:0;"><a href="/wiki/Peridot" title="Peridot"><span style="color: white; text-decoration: inherit;">Peridot</span></a>
</td>
<td style="background:#B07080; border-bottom:0;"><a href="/wiki/Pearl" title="Pearl"><span style="color: white; text-decoration: inherit;">Pink Pearl</span></a>
</td>
<td style="background:#BD559C; border-bottom:0;"><a href="/wiki/Rose_quartz" class="mw-redirect" title="Rose quartz"><span style="color: white; text-decoration: inherit;">Rose Quartz</span></a>
</td>
<td style="background:#AA4069; border-bottom:0;"><a href="/wiki/Ruby_(color)" title="Ruby (color)"><span style="color: white; text-decoration: inherit;">Ruby</span></a>
</td>
<td style="background:#2D5DA1; border-bottom:0;"><a href="/wiki/Sapphire" title="Sapphire"><span style="color: white; text-decoration: inherit;">Sapphire</span></a>
</td>
<td style="background:#832A0D; border-bottom:0;"><a href="/wiki/Topaz" title="Topaz"><span style="color: white; text-decoration: inherit;">Smokey Topaz</span></a>
</td>
<td style="background:#B56917; border-bottom:0;"><a href="/wiki/Tiger%27s_eye" title="Tiger's eye"><span style="color: white; text-decoration: inherit;">Tiger's Eye</span></a>
</td>
