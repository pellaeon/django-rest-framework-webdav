from collections import namedtuple

class Namespace(namedtuple('Namespace', ['slug', 'identifier'])):
    def prepend(self, propertyname):
        return '%s:%s' % (self.slug, propertyname)

DAVNS = Namespace(slug='d', identifier='DAV:')
