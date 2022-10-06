#!/usr/bin/env perl

$text = do { undef $/, <> };

for my $li ($text =~ m!<li>(.*?)</li>!ig) {
    my ($name, $hex) = $li =~ 
        m!>([^>]*)<br>(#[a-fA-F0-9]+)!;
    $hex = uc $hex;
    $name =~ s/^\s*//; 
    $name =~ s/\(.*\)//;
    $name =~ s/\s*$//;
    $name =~ s/['`’]//g;
    if ($name =~ m!"(.*?)"!) { 
        $name = $1; 
    }    
    print "encycolorpedia||$name|$hex|1|\n";
}


__END__
<li><a href="/006c7f" style="background-color:#006c7f;color:#fff">"New Bridge" color (Shinbashi-iro)<br>#006c7f</a></li>

<li><a href="/0048ba" style="background-color:#0048ba;color:#fff">Absolute Zero<br>#0048ba</a></li>

<li><a href="/4c2f27" style="background-color:#4c2f27;color:#fff">Acajou<br>#4c2f27</a></li>
