import jinja2
import os
import webapp2

# Application config
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
SITES_CONFIG = {
    'localhost': 'default',
    'example.com': 'example',
}

# Debug check on local or production environment
DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Dev')


class RequestHandler(webapp2.RequestHandler):
    """
    Main application logic, handles all requests.
    """
    def get(self, path='/'):
        """
        Site only serves GET method static files.
        """
        # Enforce trailing slash
        if not path.endswith("/"):
            return self.redirect(path + "/")

        # Enforce lowercase URLs
        elif path != path.lower():
            return self.redirect(path.lower())

        # Alias for domain
        domain = self.request.host.split(":")[0]
        alias = SITES_CONFIG.get(domain, 'default')

        # Templates for alias
        template_directory = os.path.join(PROJECT_ROOT, "templates/", alias)

        # Trim file path, remove slashes
        path = path[1:-1]

        # Path may refer to file or directory index
        paths = filter(None, [path, os.path.join(path, "index")])

        # We'll only look for HTML files
        filenames = map(lambda path: path + '.html', paths)

        # Look for template in domain files
        for filename in filenames:
            if os.path.exists(os.path.join(template_directory, filename)):
                template_name = filename
                break
        else:
            webapp2.abort(404)
            pass

        # Set environment to templates for alias
        jinja_env.loader = jinja2.FileSystemLoader(template_directory)
        template = jinja_env.get_template(template_name)

        # Render response, easy peasy
        self.response.write(template.render())


def handle_404(request, response, exception):
    """
    Simple handler for 404 exceptions.
    """
    template = jinja_env.get_template('404.html')
    response.write(template.render())
    response.set_status(404)


def handle_500(request, response, exception):
    """
    Simple handler for 500 exceptions.
    """
    template = jinja_env.get_template('500.html')
    response.write(template.render())
    response.set_status(500)

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape']
)

jinja_env.cache = None

application = webapp2.WSGIApplication([
    ('(.*)', RequestHandler),
], debug=DEBUG)

application.error_handlers[404] = handle_404
application.error_handlers[500] = handle_500
