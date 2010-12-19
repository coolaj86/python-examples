Rudd-O's python-inotify
====

Apparently there are a number (about 3 or so it seems) of inotify modules.

  * python-inotify
  * python-inotifyx
  * pyinotify

This example is for [Rudd-O's `python-inotify`](http://rudd-o.com/projects/python-inotify/) v0.1.0

Documentation
====

    import inotify
    help(inotify)

requires `python-pydoc` and `python-pkgutil`

BUGS
====

Doesn't seem to work more than once or twice (at least not on ARM).
After that a message appears and the process freezes

>  No handlers could be found for logger "inotify"
