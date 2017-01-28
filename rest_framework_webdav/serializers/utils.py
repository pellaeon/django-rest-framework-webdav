def find_subclasses(cls):
    return cls.__subclasses__() + [g for s in cls.__subclasses__()
                                   for g in find_subclasses(s)]

class ElementList(list):
    """
    This is a simple class used to put in identical elements,
    so that the renderer knows.
    This class does not check if the elements are REALLY identical (same shape)
    """
