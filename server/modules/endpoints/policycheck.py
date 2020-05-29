import cr
import json
from modules.endpoints.endpoint_error import EndpointError
from modules.endpoints.endpoint import Endpoint
from modules.endpoints.endpoint_response import EndpointResponse

class EndpointPolicyCheck(Endpoint):
    def __init__(self, response, rtype, params):
        self.response = response
        self.rtype = rtype
        self.params = params
        super().__init__(response)

    def parse(self):
        rtype = self.rtype
        params = self.params

        if rtype == "computer":
            return EndpointResponse(http_code=200, content="TODO!")
        elif rtype == "computer_policy":
            pol = self.db.query("FROM @all_docs WHERE type = 'policy' and id = '{}'".format(params["policyid"]))
            pol = pol["Results"][0]

            com = self.db.query("FROM @all_docs WHERE type = 'report' and source = '{}'".format(params["pcid"]))
            com = com["Results"][0]


            if self.response.query_string.find(b"ashtml") != -1:
                result = cr.policycheck(pol["data"], com, asHTML = True)
                return EndpointResponse(http_code=200, content=result, mime_type="text/html")
            else:
                result = cr.policycheck(pol["data"], com)
                return EndpointResponse(http_code=200, content=json.dumps(result))
        elif rtype == "policy":
            pol = self.db.query("FROM @all_docs WHERE type = 'policy' and id = '{}'".format(params["policyid"]))
            pol = pol["Results"][0]["data"]
            servers = []
            for sid in pol["assigned_to"]:
                servers.append({
                    "name": sid,
                    "data": self.db.query("FROM @all_docs WHERE type = 'report' and source = '{}'".format(sid))["Results"][0]
                })
                
            if self.response.query_string.find(b"ashtml") != -1:
                result = cr.policycheck(pol, servers, asHTML = True)
                return EndpointResponse(http_code=200, content=result, mime_type="text/html")
            else:
                result = cr.policycheck(pol, servers, asHTML = False)
                return EndpointResponse(http_code=200, content=json.dumps(result))
            
            return EndpointResponse(http_code=200, content="TODO!")

