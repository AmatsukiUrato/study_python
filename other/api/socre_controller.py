# -*- coding: UTF-8 -*-

from flask import Flask
from flask.json import jsonify

from other.api.statistics import calc_statistics_from_csv

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def index():
    calc_str = calc_statistics_from_csv()
    return jsonify(calc_str)


if __name__ == '__main__':
    app.run(debug=True)
