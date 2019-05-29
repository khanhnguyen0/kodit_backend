import json
import ast
import pandas as pd

from flask import Flask, jsonify, render_template
from flask_cors import CORS


app = Flask(
    __name__,
    static_folder="./build/static",
    template_folder="./build",
    static_url_path="/static",
)
CORS(app, origin=["*"])
DF = pd.read_csv("./grouped_dataset.csv")
DF["living_area_sqm"] = DF["living_area_sqm"].apply(lambda x: ast.literal_eval(x))
DF["price"] = DF["price"].apply(lambda x: ast.literal_eval(x))
DF["price_sqm"] = DF["price_sqm"].apply(lambda x: ast.literal_eval(x))


@app.route("/cluster/", methods=["GET"])
@app.route("/cluster/<cluster_id>", methods=["GET"])
def get_cluster(cluster_id=None):
    if not cluster_id:
        # return all data points
        records_json = DF.to_json(orient="records")
        return jsonify({"records": json.loads(records_json)})
    records = DF.loc[DF["cluster"] == int(cluster_id)]
    print(records["price_sqm"].values)
    if len(records) > 0:
        records_json = records.to_json(orient="records")
        print(json.loads(records_json)[0])
        return jsonify({"records": json.loads(records_json)})
    return "cluster not found", 404


@app.route("/cluster/ids/", methods=["GET"])
def get_cluster_ids():
    ids = [int(x) for x in DF["cluster"].unique().tolist()]
    return jsonify({"ids": ids})

@app.route("/", methods=["GET"])
def serve():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
