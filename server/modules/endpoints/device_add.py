import json
from modules.endpoints.endpoint_error import EndpointError
from modules.endpoints.endpoint import Endpoint
from modules.endpoints.endpoint_response import EndpointResponse

class EndpointDeviceAdd(Endpoint):
    def __init__(self, request):
        super().__init__(request)

    def parse(self):
        self.set_required_fields(["id", "name"])
        
        if not self.are_required_fields():
            return EndpointResponse(
                content=EndpointError.json(
                    EndpointError.MISSING_REQUIRED_PARAM,
                    "Missing required param",
                    {
                        "provided": self.fields,
                        "required": self.required_fields
                    }
                ),
                http_code=400
            )

        ok = self.db.put({
            "type": "device",
            "id": self.fields["id"],
            "data": {
                "name": self.fields["name"]
            }
        })
            
        return EndpointResponse(http_code=201)

