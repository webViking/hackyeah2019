#!/usr/bin/env python3
from functools import wraps
from flask import Flask, escape, request, abort, Response
from modules.endpoints.endpoint_error import EndpointError
from modules.endpoints.endpoint_response import EndpointResponse
from modules.endpoints.device_add import EndpointDeviceAdd
from modules.endpoints.policy_add import EndpointPolicyAdd
from modules.endpoints.endpoint_get import EndpointGet
from modules.endpoints.endpoint_delete import EndpointDelete
from modules.endpoints.client_recv_data import EndpointClientRecvData
from modules.endpoints.policycheck import EndpointPolicyCheck
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

current_tokens = {"asdfgh123123": True}

CLIENTS_API = "/api/client/v1/"
USER_API = "/api/web/v1/"


@app.route(USER_API + "delete", strict_slashes=False, methods=["GET"])
def delete_all():
	endp = EndpointDelete(request)
	response = endp.get_response()
	return Response(response.json_content(), mimetype=response.mime_type), response.http_code


@app.route(USER_API + "delete/<type>", strict_slashes=False, methods=["GET"])
def delete_all_of_type(type):
	endp = EndpointDelete(request, type=type)
	response = endp.get_response()
	return Response(response.json_content(), mimetype=response.mime_type), response.http_code


@app.route(USER_API + "delete/<type>/<id>", strict_slashes=False, methods=["GET"])
def delete_by_id(type, id):
	endp = EndpointDelete(request, type=type, id=id)
	response = endp.get_response()
	return Response(response.json_content(), mimetype=response.mime_type), response.http_code


# Add new obj ex. device or policy to database.
@app.route(CLIENTS_API + "add/<type>", strict_slashes=False, methods=["POST"])
def add(type):
	type = str(type).lower()
	# Add device
	if type == "device":
		endp = EndpointDeviceAdd(request)
	# Add policy
	elif type == "policy":
		endp = EndpointPolicyAdd(request)
	# Not supported type
	else:
		conent = EndpointResponse(
			content=EndpointError.json(
				EndpointError.WRONG_PARAM,
				"Type has to be device or policy, not: {}".format(type)
			),
			http_code=400
		)
		return Response(
			conent.json_content()
		), 400
	
	response = endp.get_response()	
	return Response(response.json_content(), mimetype=response.mime_type), response.http_code


# Get all of type without searching ex. get/device/ or get/policy
@app.route(USER_API + "get/<type>", strict_slashes=False, methods=["GET"])
def get_all(type):
	endp = EndpointGet(request, type=type, search_by=None)
	response = endp.get_response()
	return Response(response.json_content(), mimetype=response.mime_type), response.http_code


# Get device, policy with id ex get/device/1234 or get/policy/1234
@app.route(USER_API + "get/<type>/<id>", strict_slashes=False, methods=["GET"])
def get_by_id(type, id):
	endp = EndpointGet(request, type=type, search_by="id", search_for=id)
	response = endp.get_response()
	return Response(response.json_content(), mimetype=response.mime_type), response.http_code

# ===================== [ Policy Parser ] =====================
@app.route(USER_API + "report/computer/<pcid>", strict_slashes=False)
def report_for_computer(pcid):
	endp = EndpointPolicyCheck(request, "computer", {"pcid": pcid})
	response = endp.get_response()	
	return Response(response.json_content(), mimetype=response.mime_type), response.http_code

@app.route(USER_API + "report/computer/<pcid>/<policyid>", strict_slashes=False)
def report_for_computer_and_policy(pcid, policyid):
	endp = EndpointPolicyCheck(request, "computer_policy", {"pcid": pcid, "policyid": policyid})
	response = endp.get_response()	
	return Response(response.json_content(), mimetype=response.mime_type), response.http_code

@app.route(USER_API + "report/policy/<policyid>", strict_slashes=False)
def report_for_policy(policyid):
	endp = EndpointPolicyCheck(request, "policy", {"policyid": policyid})
	response = endp.get_response()	
	return Response(response.json_content(), mimetype=response.mime_type), response.http_code

# ====================== [ Clients ] ======================
@app.route(CLIENTS_API + "auth", strict_slashes=False, methods=["POST"])
def client_auth():
	return '{"status":true, "token":"asdfgh123123"}'


@app.route(CLIENTS_API + "data", strict_slashes=False, methods=["POST"])
def client_data():
	endp = EndpointClientRecvData(request)
	response = endp.get_response()
	return Response(response.json_content(), mimetype=response.mime_type), response.http_code

def api_client_auth_required(func):
	@wraps(func)
	def overrided(*args, **kwargs):
		global current_tokens
		
		if "Authorization" not in request.headers:
			return "No auth."
		
		token = request.headers["Authorization"]
		
		if token not in current_tokens:
			return "Bad token."
		
		#del current_tokens[token]

		return func(*args, **kwargs)
	return overrided


@app.route("/test")
#@api_client_auth_required
def testtest():
	return "OK"

@app.errorhandler(405)
def http_error_handler(error):
	
	conent = EndpointResponse(
        content=EndpointError.json(
            EndpointError.METHOD_NOT_ALLOWED,
            "Method {} is not allowed here.".format(request.method)
        ),
        http_code=405
	)
	
	return Response(
		conent.json_content()
	), 405

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
