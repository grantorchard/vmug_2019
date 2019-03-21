from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

@app.route("/api/grant")
def get_grant():
    ages = {
        "Grant": 40,
        "Elizabeth": None,
        "Audrey": 8,
        "Ewan": 4
    }
    return jsonify(ages)

@app.route("/api/cody")
def get_cody():
    ages = {
        "Cody": 34,
        "Shannon": 22,
        "Hayley": 5,
        "Morgan": 2
    }
    return jsonify(ages)

@app.route("/api/families")
def get_families():
    families = []
    families.append({
        "Cody": 34,
        "Shannon": 22,
        "Hayley": 5,
        "Morgan": 2
    })
    families.append({
        "Cody": 34,
        "Shannon": 22,
        "Hayley": 5,
        "Morgan": 2
    })
    return jsonify(families)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port="80")