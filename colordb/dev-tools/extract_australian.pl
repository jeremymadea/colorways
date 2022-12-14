#!/usr/bin/env perl
my $sub = shift;

$text = do { undef $/, <> };

for my $row ($text =~ m!<tr>(.*?)</tr>!isg) {
    next unless $row;
    my ($hex, $name) = $row =~ m!(#[a-fA-F0-9]+).*?>(\w.*?)<!;
    print "australian|$sub|$name|$hex|1|\n";
}

__END__

<tbody><tr>
<th style="width:90px">Hex</th><th>Color</th><th style="width:300px">Name</th></tr>
<tr><td>#2b3770</td><td style="background-color:#2b3770"></td><td>B11 Rich Blue</td></tr>
<tr><td>#2c3563</td><td style="background-color:#2c3563"></td><td>B12 Royal Blue</td></tr>
<tr><td>#28304d</td><td style="background-color:#28304d"></td><td>B13 Navy Blue</td></tr>
<tr><td>#28426b</td><td style="background-color:#28426b"></td><td>B14 Saphhire</td></tr>
<tr><td>#144b6f</td><td style="background-color:#144b6f"></td><td>B15 Mid Blue</td></tr>
<tr><td>#2c5098</td><td style="background-color:#2c5098"></td><td>B21 Ultramarine</td></tr>
<tr><td>#215097</td><td style="background-color:#215097"></td><td>B22 Homebush Blue</td></tr>
<tr><td>#174f90</td><td style="background-color:#174f90"></td><td>B23 Bright Blue</td></tr>
<tr><td>#1c6293</td><td style="background-color:#1c6293"></td><td>B24 Harbour Blue</td></tr>
<tr><td>#5097ac</td><td style="background-color:#5097ac"></td><td>B25 Aqua</td></tr>
<tr><td>#b7c8db</td><td style="background-color:#b7c8db"></td><td>B32 Powder Blue</td></tr>
<tr><td>#e0e6e2</td><td style="background-color:#e0e6e2"></td><td>B33 Mist Blue</td></tr>
<tr><td>#3499ba</td><td style="background-color:#3499ba"></td><td>B34 Paradise Blue</td></tr>
<tr><td>#cde4e2</td><td style="background-color:#cde4e2"></td><td>B35 Pale Blue</td></tr>
<tr><td>#5b94d1</td><td style="background-color:#5b94d1"></td><td>B41 Bluebell</td></tr>
<tr><td>#5e7899</td><td style="background-color:#5e7899"></td><td>B42 Purple Blue</td></tr>
<tr><td>#627c8d</td><td style="background-color:#627c8d"></td><td>B43 Grey Blue</td></tr>
<tr><td>#c0c0c1</td><td style="background-color:#c0c0c1"></td><td>B44 Light Grey Blue</td></tr>
<tr><td>#7db7c7</td><td style="background-color:#7db7c7"></td><td>B45 Sky Blue</td></tr>
<tr><td>#3871ac</td><td style="background-color:#3871ac"></td><td>B51 Periwinkle</td></tr>
<tr><td>#4f6572</td><td style="background-color:#4f6572"></td><td>B53 Dark Grey Blue</td></tr>
<tr><td>#3f7c94</td><td style="background-color:#3f7c94"></td><td>B55 Storm Blue</td></tr>
<tr><td>#2b3873</td><td style="background-color:#2b3873"></td><td>B61 Coral Sea</td></tr>
<tr><td>#292a34</td><td style="background-color:#292a34"></td><td>B62 Midnight Blue</td></tr>
<tr><td>#363e45</td><td style="background-color:#363e45"></td><td>B64 Charcoal</td></tr>
</tbody>


