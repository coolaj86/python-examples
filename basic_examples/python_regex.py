#!/usr/bin/python
# Filename : python_regex.py
import re

if None == re.match("c", "abcdef"):  # No match
    print "Odd but true: didn't match \"c\" in \"abcdef\""
else:
    print "matched c in abcdef"

if re.search("c", "abcdef"):
    print "As expected: found \"c\" in search of \"abcdef\""
else:
    print "did not find c in search of abcdef"

if re.search("g", "abcdef"):
    print "found g in search of abcdef"
else:
    print "As expected: did not find \"g\" in search of \"abcdef\""

# Word Boundaries are not \< and \>
# Thou shalt useth raw strings to saveth thineself from backslash hell (i.e \\\\b)
re_abcs = re.compile(r'\babc\b') # this would be /\<abc\>/ in other languages
if re_abcs.search("I know my abc's"):
    print "Not PERL alert: As found \"r'\\babc\\b'\" (i.e. \"/\\<abc\\>/\") in compiled search of \"I know my abc's\""
else:
    print "did not find '\<abc\>' in compiled search of \"I know my abc's\""
