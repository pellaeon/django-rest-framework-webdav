from __future__ import unicode_literals

from rest_framework.routers import BaseRouter

# TODO this is currently not used, because SimpleRouter should suffice
class SimpleDavRouter(BaseRouter):

    def __init__(self, trailing_slash=True):
        self.__trailing_slash = trailing_slash and '/' or ''
        super(SimpleDavRouter, self).__init__()

