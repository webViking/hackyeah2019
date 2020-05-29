import json
from modules.endpoints.endpoint_error import EndpointError
from modules.endpoints.endpoint import Endpoint
from modules.endpoints.endpoint_response import EndpointResponse

class EndpointPolicyAdd(Endpoint):
    def __init__(self, request):
        super().__init__(request)

    def parse(self):
        self.set_required_fields(["id", "name", "rules", "assigned_to"])
        
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
            "type": "policy",
            "id": self.fields["id"],
            "data": {
                "name": self.fields["name"],
                "rules": self.fields["rules"],
                "assigned_to": self.fields["assigned_to"]
            }
        })
            
        return EndpointResponse(http_code=201)

