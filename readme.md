## Google App Engine static sites

Host multiple static sites with a single [Google App Engine](https://developers.google.com/appengine/) application. Python-based, using [webapp2](https://developers.google.com/appengine/docs/python/tools/webapp2) and [jinja2](http://jinja.pocoo.org/).

Main request handler matches domains to template directories, searches for files matching paths accordingly. Basic structure inspiration by [static-appengine-hoster](https://github.com/stochastic-technologies/static-appengine-hoster), though simplified, designed for purpose.

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0)