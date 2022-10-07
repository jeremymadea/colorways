#!/usr/bin/env perl
#
# HTML code after __DATA__ token is taken from 
# https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors

#### NOTE! I manually added #FA9D5A as the hex code for Tan in the csv file.


my $text = do { undef $/; <DATA> };

for my $tr ($text =~ m!<tr[^>]*>(.*?)</tr>!isg) {
    my ($ctd,$ntd,$htd,$xtd) = $tr =~ m!<td[^>]*>(.*?)</td>!isg;

    my($name) = $ntd =~ m!\s*(\S.*\S)!;
    my($hex) = $htd =~ m!(#[A-Fa-f0-9]*)!;
    my($note) = $xtd =~ m!([^<]*)!;

    print "crayola|multicultural|$name|$hex|0|$note\n";
}


__DATA__
<tr>
<td style="background: #FDD5B1">&nbsp;
</td>
<td>Apricot
</td>
<td align="center" style="background:#E9E9E9">#FDD5B1<sup id="cite_ref-CEC_2-14" class="reference"><a href="#cite_note-CEC-2">[1]</a></sup>
</td>
<td>Produced 1958–present.<sup id="cite_ref-Welter_4-68" class="reference"><a href="#cite_note-Welter-4">[2]</a></sup>
</td></tr><tr>
<td style="background: #000000; color: white">&nbsp;
</td>
<td>Black
</td>
<td align="center" style="background:#E9E9E9">#000000<sup id="cite_ref-CEC_2-15" class="reference"><a href="#cite_note-CEC-2">[1]</a></sup>
</td>
<td>Produced 1903–present.<sup id="cite_ref-Welter_4-69" class="reference"><a href="#cite_note-Welter-4">[2]</a></sup>
</td></tr><tr>
<td style="background: #E97451; color: white">&nbsp;
</td>
<td>Burnt Sienna
</td>
<td align="center" style="background:#E9E9E9">#E97451<sup id="cite_ref-CEC_2-16" class="reference"><a href="#cite_note-CEC-2">[1]</a></sup>
</td>
<td>Produced 1903–present.<sup id="cite_ref-Welter_4-70" class="reference"><a href="#cite_note-Welter-4">[2]</a></sup>
</td></tr><tr>
<td style="background: #CA3435; color: white">&nbsp;
</td>
<td>Mahogany
</td>
<td align="center" style="background:#E9E9E9">#CA3435<sup id="cite_ref-CEC_2-17" class="reference"><a href="#cite_note-CEC-2">[1]</a></sup>
</td>
<td>Produced 1949–present.<sup id="cite_ref-Welter_4-71" class="reference"><a href="#cite_note-Welter-4">[2]</a></sup>
</td></tr><tr>
<td style="background: #FFCBA4; color; white">&nbsp;
</td>
<td>Peach
</td>
<td align="center" style="background:#E9E9E9">#FFCBA4<sup id="cite_ref-CEC_2-18" class="reference"><a href="#cite_note-CEC-2">[1]</a></sup>
</td>
<td>Produced 1903–present. Known as "Flesh Tint" (1903–1949), "Flesh" (1949–1956, 1958–1962), and "Pink Beige" (1956–1958).<sup id="cite_ref-Welter_4-72" class="reference"><a href="#cite_note-Welter-4">[2]</a></sup>
</td></tr><tr>
<td style="background: #9E5B40; color: white">&nbsp;
</td>
<td>Sepia
</td>
<td align="center" style="background:#E9E9E9">#9E5B40<sup id="cite_ref-CEC_2-19" class="reference"><a href="#cite_note-CEC-2">[1]</a></sup>
</td>
<td>Produced 1935–1944, 1958–present. Available only in bulk, 1935–1949.<sup id="cite_ref-Welter_4-73" class="reference"><a href="#cite_note-Welter-4">[2]</a></sup>
</td></tr><tr>
<td style="background: #FA9D5A; color: white">&nbsp;
</td>
<td>Tan
</td>
<td align="center" style="background:#E9E9E9">
</td>
<td>Produced 1958–present.<sup id="cite_ref-Welter_4-74" class="reference"><a href="#cite_note-Welter-4">[2]</a></sup>
</td></tr><tr>
<td style="background: #FFFFFF; color: black">&nbsp;
</td>
<td>White
</td>
<td align="center" style="background:#E9E9E9">#FFFFFF<sup id="cite_ref-CEC_2-20" class="reference"><a href="#cite_note-CEC-2">[1]</a></sup>
</td>
<td>Produced 1903–present.<sup id="cite_ref-Welter_4-75" class="reference"><a href="#cite_note-Welter-4">[2]</a></sup>
</td></tr></tbody>
