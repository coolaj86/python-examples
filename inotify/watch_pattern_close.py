#!/usr/bin/env python
from inotify import Watcher
import inotify
import sys
import re

# to test run this script and then run
# rm /tmp/foo /tmp/bar /tmp/baz /tmp/nomatch -rf
# touch /tmp/foo /tmp/bar /tmp/baz /tmp/nomatch

w = Watcher()
paths = sys.argv[1:] or ['/tmp']
patterns = [re.compile(r'^foo'), re.compile(r'^ba'), re.compile(r'az$')]


for path in paths:
    try:
        # Watch all paths recursively; only on CLOSE_WRITE
        # this seems to throw the error 'No handlers could be found for logger "inotify"'
        # when trying to watch only CLOSE_WRITE
        w.watch(path, inotify.ALL_EVENTS)
    except OSError, err:
        print >> sys.stderr, '%s: %s' % (err.filename, err.strerror)

# Quit now if we have nothing to watch
if not len(w.get_watching()):
    sys.exit(1)

# Check each event to see if any of the patterns prescribed matche
while True:
    event = w.get_next_event()
    if not inotify.CLOSE_WRITE & event.event_mask:
        continue
    dirlen = len(event.watched_filename)
    for pattern in patterns:
        # Just the filename without the leading directory
        filename = event.filename[dirlen+1:]
        if pattern.search(filename):
          print filename, "matches", pattern.pattern

