#!/usr/bin/env ruby
puts ARGV[0].scan(/\b(?!.*x\b)\w+\b/).join
