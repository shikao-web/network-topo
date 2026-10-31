from flask import Flask, redirect, url_for, jsonify, render_template
from GetNetworkTopo import GetNetworkTopo

app = Flask(__name__)

network = GetNetworkTopo()

@app.route("/")
def to_dashboard():
    return redirect(url_for("dashboard"), code=301)


@app.route("/dashboard")
def dashboard():
    return render_template("index.html")


@app.route("/api/network")
def get_network():
    return jsonify(network.graph)





if __name__ == '__main__':
    app.run(debug=True)

