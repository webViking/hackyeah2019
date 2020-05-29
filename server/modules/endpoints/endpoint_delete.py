import json
from modules.endpoints.endpoint_error import EndpointError
from modules.endpoints.endpoint import Endpoint
from modules.endpoints.endpoint_response import EndpointResponse


class EndpointDelete(Endpoint):
    def __init__(self, request, type=None, id=None):
        self.type = type
        self.id = id
        self.type = type
        super().__init__(request)

    def parse(self):

        if self.type == None:
            query = 'from @all_docs'
        elif self.id == None:
            query = 'from @all_docs where type="{}"'.format(self.type)
        else:
            query = 'from @all_docs where type="{}" and id="{}"'.format(self.type, self.id)

        data = self.db.query(query)
        for item in data["Results"]:
            self.db.delete(item["@metadata"]["@id"])

        return EndpointResponse(http_code=200)
