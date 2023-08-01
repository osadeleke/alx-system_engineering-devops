#!/usr/bin/env ruby
# checks for matching cases
from=ARGV[0].scan(/(from:[a-zA-Z0-9]*)/).join
to=ARGV[0].scan(/(to:[a-zA-Z0-9+]*)/).join
flags=ARGV[0].scan(/(flags:[0-9:-]*)/).join

$from, $to, $flags
