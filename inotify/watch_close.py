#!/usr/bin/env python
from inotify import Watcher
import inotify
import sys

w = Watcher()
paths = sys.argv[1:] or ['/tmp']

for path in paths:
    try:
        # Watch all paths recursively, and all events on them.
        w.watch(path, inotify.ALL_EVENTS)
    except OSError, err:
        print >> sys.stderr, '%s: %s' % (err.filename, err.strerror)

# If we have nothing to watch, don't go into the read loop, or we'll
# sit there forever.

if not len(w.get_watching()):
    sys.exit(1)

while True:
    event = w.get_next_event()
    if not inotify.CLOSE_WRITE & event.event_mask:
        continue
    print event.event_mask
    print event.filename
    print event.watched_filename
    print event
    #print repr(evt.fullpath), ' | '.join(inotify.decode_mask(evt.mask))
