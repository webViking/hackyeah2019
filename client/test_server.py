from flask import Flask, request
from flask_cors import CORS
import json
import uuid
import random

app = Flask(__name__)
CORS(app)


@app.route('/api/client/v1/auth', methods = ["POST"])
def api_client_auth():
	data = request.get_data().decode("UTF-8")
	data = json.loads(data)
	
	if data["uuid"] == "123" and data["password"] == "test":
		return json.dumps({
			"status": True,
			"token": "asdfgh"
		})
	else:
		return json.dumps({
			"status": False,
			"token": None
		})

@app.route('/api/v1/policies/')
def get_policies():
	names = ["boat_horse","toolbox_prints","boat_elevator","leash_bird","soda_printer","prints_plus","light_saber_kitty","cat_floppy_disk","cone_printer","horse_breakfast"]

	pc_names = ["whale_shelf","breakfast_floppy_disk","video_games_poop","sink_breakfast","horse_horse","system_solar","soda_ring","shelf_bbq","body_cone","ice_cream_kitty"]

	out = {
		"policies": []
	}

	for i in range(random.randint(2, 50)):
		out["policies"].append({
			"id": str(uuid.uuid4()),
			"name": random.choice(names).replace("_", " ").title(),
			"rules": [{'rule objects will be here': None}] * random.randint(1, 20),
			"assigned": [
				{
					"name": random.choice(pc_names),
					"uuid": str(uuid.uuid4())
				}
			]
		})
	
	return json.dumps(out)

@app.route('/api/client/v1/data', methods = ["POST", "GET"])
def hello():
	if request.method == "POST":
		print("POST")
		data = request.get_json()
		print(data)
		with open("data.json", "w", encoding = "UTF-8") as f:
			json.dump(data, f)
	else:
		print("GET")
	return "Hello World!"


if __name__ == '__main__':
	app.run('0.0.0.0')