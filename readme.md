## Google App Engine static sites

Host multiple static sites with a single [Google App Engine](https://developers.google.com/appengine/) application. Python-based, using [webapp2](https://developers.google.com/appengine/docs/python/tools/webapp2) and [jinja2](http://jinja.pocoo.org/).

Main request handler matches domains to template directories, searches for files matching paths accordingly. Basic structure inspired by [static-appengine-hoster](https://github.com/stochastic-technologies/static-appengine-hoster), simplified and redesigned for purpose.

### Running the application

1. Run using the development server (in current directory)

        $ dev_appserver.py .

    Configure `--address` and `--port` to suit your needs.

2. Add a host entry to demo locally

        $ 127.0.0.1 example.com

3. Visit corresponding URLs in the browser, e.g. [http://localhost:8080](http://localhost:8080) and [http://example.com:8080](http://example.com:8080)

This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0)