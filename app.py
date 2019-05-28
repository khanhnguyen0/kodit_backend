import json
import pandas as pd

from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origin=["*"])
DF = pd.read_csv("./grouped_dataset.csv")


@app.route("/cluster/", methods=["GET"])
@app.route("/cluster/<cluster_id>", methods=["GET"])
def get_cluster(cluster_id=None):
    if not cluster_id:
        # return all data points
        records_json = DF.to_json(orient="records")
        return jsonify({"records": json.loads(records_json)})
    records = DF.loc[DF["cluster"] == int(cluster_id)]
    if len(records) > 0:
        records_json = records.to_json(orient="records")
        return jsonify({"records": json.loads(records_json)})
    return "cluster not found", 404


@app.route("/cluster/ids/", methods=["GET"])
def get_cluster_ids():
    ids = list(DF["cluster"].unique())
    return jsonify({"ids": ids})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
