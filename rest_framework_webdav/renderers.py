from __future__ import unicode_literals

from rest_framework.renderers import BaseRenderer, BrowsableAPIRenderer

class WebDAVXMLRenderer(BaseRenderer):
    """
    Renders WebDAV-compliant XML
    """

    media_type = 'application/xml'
    format = 'xml'
    
class BrowsableWebDAVXMLRenderer(BrowssableAPIRenderer):
    """
    Renders XML in HTML text, with links. For easy debugging.
    """

    media_type = 'text/html'
    format = 'api'

    def get_content(self, renderer, data,
            accepted_media_type, renderer_context):
        pass #TODO
