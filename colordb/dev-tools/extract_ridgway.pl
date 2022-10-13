#!/usr/bin/env perl
#my $sub = shift;

$text = do { undef $/, <> };

for my $row ($text =~ m!("name".*?plate[^,]*)!isg) {
    my ($name) = $row =~ /"name":\s*"([^"]*)/;
    my ($hex)  = $row =~ /"hex":\s*"([^"]*)/;
    my ($note) = $row =~ /"plate":\s*"([^"]*)/;
    next unless $hex; 
    $hex = uc $hex;
    print "Ridgway||$name|$hex|0|Plate $note\n";
}

__END__
