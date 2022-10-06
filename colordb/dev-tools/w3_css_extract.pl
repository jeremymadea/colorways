#!/usr/bin/env perl

while (<>) { 
    #my ($w3, $set, $name, $hex) = m!
    #    \.(w3)-([^-]*)-([a-z]*)
    #    .*background\s*:\s*(#[a-fA-F0-9]{6})
    #!ix;
    my ($w3, $set, $name, $hex) = m!
        \.(w3)-([^-]*)-([-a-z]*).*background-color\s*:\s*(\#[a-fA-F0-9]{6})    
        
    !ix;
    $name =~ s/-/ /g;
    print "w3|$set|$name|$hex|1|\n";
}

__END__

><tr>
<td style="background:#C39953; border-bottom:0; width:12%;">Aztec Gold
</td>
<td style="background:#A17A74; border-bottom:0; width:12%;">Burnished Brown
</td>
<td style="background:#6D9BC3; border-bottom:0; width:12%;">Cerulean Frost
</td>
<td style="background:#CD607E; border-bottom:0; width:12%;">Cinnamon Satin
</td></tr>
<tr>

