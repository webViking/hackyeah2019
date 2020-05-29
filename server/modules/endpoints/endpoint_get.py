import json
from modules.endpoints.endpoint_error import EndpointError
from modules.endpoints.endpoint import Endpoint
from modules.endpoints.endpoint_response import EndpointResponse


class EndpointGet(Endpoint):
    def __init__(self, request, type=None, search_by=None, search_for=None):
        if search_by != None:
            self.search_by = str(search_by).lower()
        else:
            self.search_by = search_by
        self.search_for = search_for
        self.type = type
        super().__init__(request)

    def parse(self):
        
        if self.type != None:
            search = 'type = "{}"'.format(self.type)
        else:
            search = ''
        
        if self.search_by != None:
            search += ' and {} = "{}"'.format(self.search_by, self.search_for)
        else:
            search += ''

        print("FROM @all_docs where {}".format(search))

        data = self.db.query("FROM @all_docs where {}".format(search))

        return EndpointResponse(content=data["Results"], http_code=200)
