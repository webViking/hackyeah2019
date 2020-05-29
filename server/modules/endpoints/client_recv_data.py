import json
from modules.endpoints.endpoint_error import EndpointError
from modules.endpoints.endpoint import Endpoint
from modules.endpoints.endpoint_response import EndpointResponse

class EndpointClientRecvData(Endpoint):
    def __init__(self, response):
        super().__init__(response)

    def parse(self):
        self.set_required_fields(["type", "station_uuid", "status", "data"])
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

        raw_data = self.fields
        
        if not raw_data["status"]:
            print("app returned bad status!!!")
            return EndpointResponse(
                content=EndpointError.json(
                    EndpointError.MISSING_REQUIRED_PARAM,
                    "App returned bad status."
                ),
                http_code=400
            )

        #TODO: Save to DB
        db_data = {
            "type": "report",
            "source": raw_data["station_uuid"],
            "data": raw_data["data"]
        }

        self.db.put(db_data)

        return EndpointResponse(http_code=201)

