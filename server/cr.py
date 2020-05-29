import json

def rulecheckall(reqs, serverdata):
	def check_rule(rule):
		if rule["namespace"].find(".") != -1:
			return False, "Nested namespaces not supported."
		
		if rule["namespace"] not in serverdata:
			return False, "No such namespace."

		namespace = serverdata[rule["namespace"]]
		robj = None
		if rule["object"] != "":
			for cobj in namespace:
				if eval("cobj" + rule["object"]):
					robj = cobj
					break
		
		if not robj:
			return False, "Object not found"
		
		try:
			return robj[rule["requirement"]["key"]] == rule["requirement"]["value"]
		except:
			return False, "Exception during requirement check!"

	out = {
		"name": reqs["name"],
		"all_ok": True,
		"results": []
	}

	for rule in reqs["rules"]:
		result = check_rule(rule)
		error = (type(result) != bool)
		print(rule["name"], result)
		out["results"].append({
			"name": rule["name"],
			"result": result,
			"error": error
		})

		if not result or error:
			out["all_ok"] = False
		
	return out
	

def policycheck(policy, serverdata, asHTML = False):
	if type(serverdata) == list:
		out = []
		for item in serverdata:
			reqs = policy
			item2 = item["data"]["data"] 
			out.append({
				"name": item["name"],
				"value": rulecheckall(reqs, item2)
			})
	else:
		reqs = policy
		serverdata = serverdata["data"] 
		out = rulecheckall(reqs, serverdata)

	if not asHTML:
		return out
		
	with open("report.html", "r") as f:
		template = f.read()

		if type(serverdata) != list:
			template = template.replace("{REPORT_NAME}", out["name"])
		else:
			template = template.replace("{REPORT_NAME}", "")
		content = ""
		if type(serverdata) != list:
			for i, r in enumerate(out["results"]):
				if r["error"]:
					content += "<tr>"
					content += "<td>{}</td>".format(i+1)
					content += "<td>{}</td>".format(r["name"])
					content += "<td>{}</td>".format('<div class="i_failed>Failed</div>')
					content += "<td>{}</td>".format(r["result"])
					content += "</tr>"
				else:
					content += "<tr>"
					content += "<td>{}</td>".format(i+1)
					content += "<td>{}</td>".format(r["name"])
					if not r["result"]:
						content += "<td>{}</td>".format('<div class="i_failed">Failed</div>')
					else:
						content += "<td>{}</td>".format('<div class="i_passed">Passed</div>')
					content += "<td></td>"
					content += "</tr>"
		else:
			for item in out:
				for i, r in enumerate(item["value"]["results"]):
					i = item["name"]
					if r["error"]:
						content += "<tr>"
						content += "<td>{}</td>".format(i)
						content += "<td>{}</td>".format(r["name"])
						content += "<td>{}</td>".format('<div class="i_failed>Failed</div>')
						content += "<td>{}</td>".format(r["result"])
						content += "</tr>"
					else:
						content += "<tr>"
						content += "<td>{}</td>".format(i)
						content += "<td>{}</td>".format(r["name"])
						if not r["result"]:
							content += "<td>{}</td>".format('<div class="i_failed">Failed</div>')
						else:
							content += "<td>{}</td>".format('<div class="i_passed">Passed</div>')
						content += "<td></td>"
						content += "</tr>"

		template = template.replace("{CONTENT}", content)

		return template

if __name__ == "__main__":
	with open("example_reqs.json", "r") as f:
		reqs = json.load(f)

	with open("data.json", "r") as f:
		serverdata = json.load(f)

	with open("data2.json", "r") as f:
		serverdata2 = json.load(f)

	with open("oooo.json", "w") as f:
		# json.dump(policycheck(reqs, serverdata), f)
		json.dump(policycheck(reqs["data"], [
			{"data": serverdata, "name": "serverdata"},
			{"data": serverdata2, "name": "serverdata2"}
		]), f)

	with open("oooo.html", "w") as f:
		# json.dump(policycheck(reqs, serverdata), f)
		f.write(policycheck(reqs["data"], [
			{"data": serverdata, "name": "serverdata"},
			{"data": serverdata2, "name": "serverdata2"}
		], asHTML = True))