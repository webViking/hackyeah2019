from modules.endpoints.endpoint_response import EndpointResponse
from modules.raven_interface import RavenInterface

class Endpoint:

    # Use internal field as param (param depends of function)
    USE_SELF = 0

    def __init__(self, request):
        self.request = request
        
        self.http_code = None
        self.mime_type = "application/json"

        data = self.request.get_json()
        if data != None:
            self.fields = data
        else:
            self.fields = []
        self.required_fields = []

        self.db = RavenInterface()

    def set_http_code(self, code):
        self.http_code = code
        
    def set_mime_type(self, mime):
        self.mime_type = mime
        
    def set_required_fields(self, fields = []):
        self.required_fields = fields

    def are_required_fields(self):

        for field in self.required_fields:
            if field not in self.fields:
                return False

        return True

    def get_response(self):
        return self.parse()
