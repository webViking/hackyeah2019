import requests

class RavenInterface:

    IP_ADDR = "localhost"
    PORT = "9090"
    DB = "orlen"

    def __init__(self):
        self.url = "http://{}:{}/databases/{}".format(self.IP_ADDR, self.PORT, self.DB)
    
    def query(self, query_str):
        data = {
            "query": query_str,
            "parameters": "{}",
			"start": "0",
			"metadataOnly": "false"
        }
        
        r = requests.get(self.url + "/queries", params=data)
        
        print("Database API response code: {}".format(r.status_code))
        if r.status_code != 200:
            return False
        
        return r.json()

    def put(self, json_data):
        data = {
            "Commands": [
                {
                    "Document": json_data,
                    "Id": "",
                    "Type": "PUT"
                }
            ]
        }
        r = requests.post(self.url + "/bulk_docs", json=data)
        print("Database API response code: {}".format(r.status_code))
        if r.status_code != 200:     
            return False

        return True

    def delete(self, doc_id):
        r = requests.post(self.url + "/bulk_docs", json = {
            "Commands": [
                {
                    "Id": doc_id,
                    "Type": "DELETE"
                }
            ],
            "TransactionMode": "SingleNode"
        })
        print("Database API response code: {}".format(r.status_code))
        if r.status_code != 200:     
            return False

        return True
