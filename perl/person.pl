#!/usr/bin/env perl5
use strict;

# tl;dr I'm too rusty and have too much else to do to finish this, but
# the way structures get built in Perl using references makes it a bit
# more clunky that in JS and maybe the same as in Python.

use JSON qw();
use Data::Dumper;

my $json_text = do {
    open(my $fh, "input_json/patient.input.json") or die "can't open file";
    local $/;
    <$fh>
};

#print($json_text);
my $json = JSON->new;
my $data = $json->decode($json_text);
#print Dumper($data);

print("race:       ", Dumper( ($data)['extension'] ));
print("----------------------");
print("race:       ", Dumper( ($data)['extension'](0)['extension'] ));

#print("race:       ", data["extension"][0]["extension"][0]["valueCoding"]["display"])

#my %dest;
#dest.part_a[1] = {"person": null, "addr": null, "event":null}


#for ( @{data$->{address}} ) {
#    print $_, "\n";
#}
#    print("person_id:  ", data["id"])
#    print("race:       ", data["extension"][0]["extension"][0]["valueCoding"]["display"])
    # if the output structure is deeper, you have to generate/create/"vivify" the intermediate structures.
    # contrived, but like this:
    # (Perl implicitly does the creation with only something similar to the last line.)
    #dest = { "part_a": null, "part_b": null, "part_c": null }
    #dest.part_a = [null, null, null]
    #dest.part_a[1] = {"person": null, "addr": null, "event":null}
    #dest.part_a[1].person = convert()}

