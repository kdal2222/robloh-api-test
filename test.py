from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

API_KEY = os.getenv("ROBLOXAPIBSS")
UNIVERSE_ID = "8838594486"

@app.route("/get", methods=["GET"])
def get_data():
    key = str(request.args.get("key"))
    DATASTORE_NAME = str(request.args.get("DataStore"))
    url = f"https://apis.roblox.com/datastores/v1/universes/{UNIVERSE_ID}/standard-datastores/datastore/entries/entry"
    headers = {"x-api-key": API_KEY}
    params = {"datastoreName": DATASTORE_NAME, "entryKey": key}

    r = requests.get(url, headers=headers, params=params)
    return (r.text, r.status_code, r.headers.items())

@app.route("/set", methods=["POST"])
def set_data():
    data = request.json
    key = data.get("key")
    value = data.get("value")

    url = f"https://apis.roblox.com/datastores/v1/universes/{UNIVERSE_ID}/standard-datastores/datastore/entries/entry"
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    params = {"datastoreName": DATASTORE_NAME, "entryKey": key}
    body = {"value": str(value)}

    r = requests.post(url, headers=headers, params=params, json=body)
    return (r.text, r.status_code, r.headers.items())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
