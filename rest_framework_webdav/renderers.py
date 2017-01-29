from __future__ import unicode_literals


from django.utils import six
from django.utils.xmlutils import SimplerXMLGenerator
from django.utils.six.moves import StringIO
from django.utils.encoding import smart_text
from rest_framework.renderers import BaseRenderer, BrowsableAPIRenderer
from rest_framework_webdav.serializers.utils import ElementList, ElementGroup

class WebDAVXMLRenderer(BaseRenderer):
    """
    Renders WebDAV-compliant XML
    """

    media_type = 'application/xml'
    format = 'xml'
    charset = 'utf-8'
    item_tag_name = 'list-item'
    root_tag_name = 'multistatus'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders `data` into serialized XML.
        """
        if data is None:
            return ''

        stream = StringIO()

        xml = SimplerXMLGenerator(stream, self.charset)
        xml.startDocument()
        xml.startElement(self.root_tag_name, {})

        self._to_xml(xml, data)

        xml.endElement(self.root_tag_name)
        xml.endDocument()
        return stream.getvalue()

    def _to_xml(self, xml, data):
        if isinstance(data, (list, tuple)):
            for item in data:
                self._to_xml(xml, item)

        elif isinstance(data, dict):
            for key, value in six.iteritems(data):
                if isinstance(value, ElementList):
                    for innerval in value:
                        xml.startElement(key, {})
                        self._to_xml(xml, innerval)
                        xml.endElement(key)
                if isinstance(value, ElementGroup):
                    for innerkey, innerval in value.items():
                        xml.startElement(key, {})#key=<propstat>
                        self._to_xml(xml, innerval)
                        xml.startElement(innerkey[0], {})
                        self._to_xml(xml, innerkey[1])
                        xml.endElement(innerkey[0])
                        xml.endElement(key)

                else:
                    xml.startElement(key, {})
                    self._to_xml(xml, value)
                    xml.endElement(key)

        elif data is None:
            # Don't output any value
            pass

        else:
            xml.characters(smart_text(data))

class BrowsableWebDAVXMLRenderer(BrowsableAPIRenderer):
    """
    Renders XML in HTML text, with links. For easy debugging.
    """

    media_type = 'text/html'
    format = 'api'

    def get_content(self, renderer, data,
            accepted_media_type, renderer_context):
        pass #TODO
