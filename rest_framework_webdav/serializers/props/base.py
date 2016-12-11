class PropNamespace(object):
    slug = None
    identifier = None

    def __init__(self, resource):
        if not isinstance(resource, BaseResource):
            raise TypeError("You need to feed in an instance of BaseResource "
                "like this: PropNamespace(res_obj) ")
        self.resource = resource

    def get_prop_list(self):
        return [f for f in inspect.getmembers(self.__class__, predicate=inspect.ismethod) if f.__name__.startswith('prop_')]

    def get_all_prop_dict(self):
        """
        Get all props, each prop in a dict like this:
        {
            name: "getlastmodified",
            live: True,
            status: "HTTP/1.1 404 Not Found",
            value: "Mon, 21 Nov 2016 18:19:28 GMT",
            namespace: "d"
        }
        """
        all_list = []
        print(self.get_prop_list())
        for prop in self.get_prop_list():
            ret = prop(self)
            ret['name'] = prop.__name__
            ret['namespace'] = self.slug
            all_list.append(ret)

        return all_list

"""
class ExampleNamespace(PropNamespace):
    slug = 'e'
    identifier = "http://example.com/blablans"
"""

def get_namespace_classes():
    return PropNamespace.__subclasses__() + [g for s in PropNamespace.__subclasses__()
                                   for g in all_subclasses(s)]
