import json

class EndpointResponse:
    def __init__(self, content={}, http_code=200, mime_type="application/json"):
        self.http_code = http_code
        self.content = content
        self.mime_type = mime_type

        if http_code in [200,201]:
            self.general_status = True
        else:
            self.general_status = False

        self.ocontent = self.content
        self.content = {
            "success": self.general_status,
            "data": self.content
        }

    def json_content(self):
        if self.mime_type != "application/json":
            return self.ocontent
        return json.dumps(self.content)
